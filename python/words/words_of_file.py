from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from typing import Dict

import os
import nltk
import re
import string
import enchant
import pickle

from util.util import rel_path_from_abs_path

nltk.download('punkt')
nltk.download('stopwords')

class WordUnstemDicts:
    def __init__(self):
        self.word_dict = {}
        self.unstem_dict = {}


word_unstem_dicts = WordUnstemDicts()


en = enchant.Dict("en_US")
de = enchant.Dict("de_DE")
fr = enchant.Dict("fr_FR")


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


def add_to_unstem_dict(word: str, stemmed_word: str):
    if stemmed_word in word_unstem_dicts.unstem_dict:
        if len(word) < len(word_unstem_dicts.unstem_dict[stemmed_word]):
            word_unstem_dicts.unstem_dict[stemmed_word] = word
    else:
        word_unstem_dicts.unstem_dict[stemmed_word] = word


def stemming(data):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        stemmed_word = stemmer.stem(w)
        add_to_unstem_dict(w, stemmed_word)
        new_text = new_text + " " + stemmer.stem(w)

    return new_text


def unstem(word):
    return word_unstem_dicts.unstem_dict[word]


def is_en_de_fr(word):
    return en.check(word) or de.check(word) or fr.check(word)


def filter_non_en_de_fr_words(data):
    tokens = word_tokenize(str(data))
    return " ".join(list(filter(lambda w: is_en_de_fr(unstem(w)), tokens)))


def get_words_of_file(file_path):
    try:
        shakes = open(file_path, 'r')
        text = shakes.read()
        no_punctuation = text.translate(string.punctuation)
        only_a_to_z = re.sub('[^A-Za-z ]+', ' ', no_punctuation)
        camel_case_split = split_camel_case(only_a_to_z)
        camel_case_split_no_single_chars = remove_single_chars(camel_case_split)
        camel_case_split_no_single_chars_no_stop_words = remove_stop_words(camel_case_split_no_single_chars)
        camel_case_split_no_single_chars_no_stop_words_stemmed = stemming(camel_case_split_no_single_chars_no_stop_words)
        camel_case_split_no_single_chars_no_stop_words_stemmed_only_en_de_fr = filter_non_en_de_fr_words(camel_case_split_no_single_chars_no_stop_words_stemmed)
        return camel_case_split_no_single_chars_no_stop_words_stemmed_only_en_de_fr
    except:
        return ""


def is_no_dot_file(file_path):
    return len(list(filter(lambda part: part.startswith("."), file_path.split("/")))) == 0


def has_no_excluded_extension(file_path):
    extension = file_path.split(".")[-1]
    return extension.lower() not in ["jpg", "jpeg", "png", "bmp", "csv"]


def is_included(file_path):
    return is_no_dot_file(file_path) and has_no_excluded_extension(file_path)


def fill_word_unstem_dicts(doc_path):
    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = subdir + os.path.sep + file
            if is_included(file_abs_path):
                file_rel_path = rel_path_from_abs_path(doc_path, file_abs_path)
                print(f">>> {file_rel_path}")
                words_of_file = get_words_of_file(file_abs_path)
                print(f"\t[{words_of_file}]")
                if len(words_of_file) > 0:
                    word_unstem_dicts.word_dict[file_rel_path] = words_of_file
                print(f"<<< {file_rel_path}")
    print("!!!! FINISHED !!!")


def read_or_create_word_unstem_dict(doc_path, dict_path, name) -> WordUnstemDicts:
    word_unstem_dicts_path = os.path.join(dict_path, f"word_unstem_dicts.{name}.pickle")
    if os.path.exists(word_unstem_dicts_path):
        pickle_file = open(word_unstem_dicts_path, "rb")
        return pickle.load(pickle_file)
    else:
        fill_word_unstem_dicts(doc_path)
        pickle_file = open(word_unstem_dicts_path, "wb")
        pickle.dump(word_unstem_dicts, pickle_file)
        return word_unstem_dicts


