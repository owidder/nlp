import os
import pickle
import re
import sys
import traceback

import enchant
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from util.util import rel_path_from_abs_path, open_file_for_writing_with_path_creation
from words.term_filter_level import TermFilterLevel
from words.isTerm import is_term_hard, is_term_medium, is_term_soft, init_term_infos

nltk.download('punkt')
nltk.download('stopwords')


en = enchant.Dict("en_US")
de = enchant.Dict("de_DE")


def split_camel_case(name):
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', name).lower()


def remove_single_chars(string):
    return ' '.join([w for w in string.split() if len(w) > 1])


def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text


def add_to_unstem_dict(word: str, stemmed_word: str, unstem_dict):
    if stemmed_word in unstem_dict:
        if len(word) < len(unstem_dict[stemmed_word]):
            unstem_dict[stemmed_word] = word
    else:
        unstem_dict[stemmed_word] = word


def stemming(data, unstem_dict):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for word in tokens:
        stemmed_word = stemmer.stem(word)
        print(f"stem\t{word}\t{stemmed_word}")
        add_to_unstem_dict(word, stemmed_word, unstem_dict)
        new_text = new_text + " " + stemmer.stem(word)

    return new_text


def is_en_de(word):
    result = en.check(word) or de.check(word)
    print(f"isword\t{word}\t{result}")
    return result


def filter_non_en_de_words(data):
    tokens = word_tokenize(str(data))
    return " ".join(list(filter(lambda word: is_en_de(word), tokens)))


def get_words_of_file(file_path, unstem_dict):
    try:
        shakes = open(file_path, 'r')
        text = shakes.read()
        only_a_to_z = re.sub('[^A-Za-z ]+', ' ', text)
        camel_case_split = split_camel_case(only_a_to_z)
        camel_case_split_no_single_chars = remove_single_chars(camel_case_split)
        camel_case_split_no_single_chars_no_stop_words = remove_stop_words(camel_case_split_no_single_chars)
        camel_case_split_no_single_chars_no_stop_words_only_en_de = filter_non_en_de_words(camel_case_split_no_single_chars_no_stop_words)
        camel_case_split_no_single_chars_no_stop_words_only_en_de_stemmed = stemming(camel_case_split_no_single_chars_no_stop_words_only_en_de, unstem_dict)
        return camel_case_split_no_single_chars_no_stop_words_only_en_de_stemmed
    except:
        print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        traceback.print_exc(file=sys.stdout)
        return ""


def is_no_dot_file(file_path):
    return len(list(filter(lambda part: part.startswith("."), file_path.split("/")))) == 0


def has_no_excluded_extension(file_path):
    extension = file_path.split(".")[-1]
    return extension.lower() not in ["jpg", "jpeg", "png", "bmp", "csv"]


def is_included(file_path):
    return is_no_dot_file(file_path) and has_no_excluded_extension(file_path)


def unstem(word_stemmed, unstem_dict):
    print(f"unstem\t{word_stemmed}\t{unstem_dict[word_stemmed]}")
    return unstem_dict[word_stemmed]


def unstemAndFilterNonTerms(word_stemmed, unstem_dict, filter_level: TermFilterLevel):
    unstemmed = unstem(word_stemmed, unstem_dict)
    if filter_level == TermFilterLevel.NONE:
        return unstemmed
    elif filter_level == TermFilterLevel.SOFT:
        return is_term_soft(unstemmed)
    pass


def unstem_word_dict(word_dict_stemmed, unstem_dict):
    return {file_rel_path: " ".join([unstem(word_stemmed, unstem_dict) for word_stemmed in words_stemmed.split()]) for file_rel_path, words_stemmed in word_dict_stemmed.items()}


def filter_word(word: str, filter_level: TermFilterLevel):
    if filter_level == TermFilterLevel.SOFT:
        return is_term_soft(word)
    elif filter_level == TermFilterLevel.MEDIUM:
        return is_term_medium(word)
    elif filter_level == TermFilterLevel.HARD:
        return is_term_hard(word)
    else:
        return word


def filter_word_dict(word_dict, filter_level: TermFilterLevel):
    if filter_level == TermFilterLevel.NONE:
        return word_dict

    return {file_rel_path: " ".join([filter_word(word, filter_level) for word in words]) for file_rel_path, words in word_dict.items()}


def create_word_dict(doc_path, filter_level: TermFilterLevel):
    word_dict_stemmed = {}
    unstem_dict = {}
    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = subdir + os.path.sep + file
            if is_included(file_abs_path):
                file_rel_path = rel_path_from_abs_path(doc_path, file_abs_path)
                words_of_file = get_words_of_file(file_abs_path, unstem_dict)
                if len(words_of_file) > 0:
                    word_dict_stemmed[file_rel_path] = words_of_file
    word_dict = unstem_word_dict(word_dict_stemmed, unstem_dict)
    filtered_word_dict = filter_word_dict(word_dict, filter_level)
    return filtered_word_dict


def read_or_create_word_dict(doc_path, dict_path, name, term_infos_name, term_infos_path, filter_level: TermFilterLevel):
    word_dict_path = os.path.join(dict_path, f"word_dict.{name}-{term_infos_name}-{filter_level.value}.pickle")
    if os.path.exists(word_dict_path):
        pickle_file = open(word_dict_path, "rb")
        word_dict = pickle.load(pickle_file)
        return word_dict
    else:
        init_term_infos(term_infos_path, term_infos_name)
        word_dict = create_word_dict(doc_path, filter_level)
        pickle_file = open_file_for_writing_with_path_creation(word_dict_path, 'wb')
        pickle.dump(word_dict, pickle_file)
        return word_dict


