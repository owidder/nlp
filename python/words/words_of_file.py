import os
import pickle
import re
import sys
import traceback

import enchant
import nltk
import ssl
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from python.util.util import rel_path_from_abs_path, open_file_for_writing_with_path_creation
from python.util.dict_util import merge_dict2_into_dict1, create_file_name
from python.stackexchange.stackexchange import remove_non_stackexchange
from python.get_args import get_bool_env_var, WITH_STEMMING, DO_REMOVE_NON_CHARS, DO_REMOVE_SINGLE_CHARS, DO_REMOVE_STOP_WORDS, DO_FILTER_NON_EN_DE_WORDS, DO_SPLIT_CAMEL_CASE


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')


en = enchant.Dict("en_US")
de = enchant.Dict("de_DE")


def split_camel_case(name):
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', name)


def remove_short_words(string, min_length):
    return ' '.join([w for w in string.split() if len(w) >= min_length])


def remove_stop_words(data, remove_de=True, remove_en=True):
    stop_words_en = stopwords.words('english') if remove_en else []
    stop_words_de = stopwords.words('german') if remove_de else []
    stop_words = stop_words_en + stop_words_de
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w.lower() not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text


def add_to_unstem_dict(word: str, stemmed_word: str, unstem_dict):
    if stemmed_word in unstem_dict:
        if len(word) < len(unstem_dict[stemmed_word]):
            unstem_dict[stemmed_word] = word
    else:
        unstem_dict[stemmed_word] = word


def stemming(data):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for word in tokens:
        stemmed_word = stemmer.stem(word)
        print(f"stem\t{word}\t{stemmed_word}")
        new_text = new_text + " " + stemmer.stem(word)

    return new_text


def is_en_de(word):
    result = en.check(word) or de.check(word)
    print(f"isword\t{word}\t{result}")
    return result


def filter_non_en_de_words(data):
    tokens = word_tokenize(str(data))
    return " ".join(list(filter(lambda word: is_en_de(word), tokens)))


def get_tags_of_file(text):
    stackexchange_tags = remove_non_stackexchange(text)
    stackexchange_tags = remove_stop_words(stackexchange_tags)
    return stackexchange_tags


def get_words_of_file(text, with_stemming=None,
                      do_remove_non_chars=False,
                      do_split_camel_case=False,
                      do_remove_stop_words=False,
                      do_filter_non_en_de_words=False,
                      do_remove_single_chars=False):
    words_of_file = text.lower()
    words_of_file = re.sub('[^a-z ]+', ' ', words_of_file) if get_bool_env_var(DO_REMOVE_NON_CHARS, do_remove_non_chars) else text
    words_of_file = split_camel_case(words_of_file) if get_bool_env_var(DO_SPLIT_CAMEL_CASE, do_split_camel_case) else words_of_file
    words_of_file = remove_short_words(words_of_file, min_length=4) if get_bool_env_var(DO_REMOVE_SINGLE_CHARS, do_remove_single_chars) else words_of_file
    words_of_file = remove_stop_words(words_of_file) if get_bool_env_var(DO_REMOVE_STOP_WORDS, do_remove_stop_words) else words_of_file
    words_of_file = filter_non_en_de_words(words_of_file) if get_bool_env_var(DO_FILTER_NON_EN_DE_WORDS, do_filter_non_en_de_words) else words_of_file
    words_of_file = stemming(words_of_file) if get_bool_env_var(WITH_STEMMING, with_stemming) else words_of_file
    return words_of_file


def get_words_and_tags_of_file(file_path):
    try:
        print(file_path)
        shakes = open(file_path, 'r')
        text = shakes.read()
        return get_words_of_file(text), get_tags_of_file(text)
    except:
        print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        traceback.print_exc(file=sys.stdout)
        return "", ""


def is_no_dot_file(file_path):
    return len(list(filter(lambda part: part.startswith("."), file_path.split("/")))) == 0


def has_no_excluded_extension(file_path):
    extension = file_path.split(".")[-1]
    return extension.lower() not in ["jpg", "jpeg", "png", "bmp", "csv"]


def has_included_extension(file_path):
    parts = file_path.split(".")
    if len(parts) > 2:
        extension = ".".join(parts[-2:])
        return extension.lower() in ["py.utf8", "js.utf8", "json.utf8", "txt.utf8"]
    return False


def is_included(file_path):
    return is_no_dot_file(file_path) and has_included_extension(file_path)


def unstem(word_stemmed, unstem_dict):
    print(f"unstem\t{word_stemmed}\t{unstem_dict[word_stemmed]}")
    return unstem_dict[word_stemmed]


def unstem_word_dict(word_dict_stemmed, unstem_dict):
    return {file_rel_path: " ".join([unstem(word_stemmed, unstem_dict) for word_stemmed in words_stemmed.split()]) for file_rel_path, words_stemmed in word_dict_stemmed.items()}


def create_word_and_tags_dict(doc_path):
    print("create_word_dict:", locals())
    word_dict = {}
    tags_dict = {}
    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = subdir + os.path.sep + file
            if is_included(file_abs_path):
                try:
                    file_rel_path = rel_path_from_abs_path(doc_path, file_abs_path)
                    words_of_file, tags_of_file = get_words_and_tags_of_file(file_abs_path)
                    if len(words_of_file) > 0:
                        word_dict[file_rel_path] = words_of_file
                    if len(tags_of_file) > 0:
                        tags_dict[file_rel_path] = tags_of_file
                except:
                    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
                    traceback.print_exc(file=sys.stdout)
    return word_dict, tags_dict


def read_word_dict(word_dict_path):
    pickle_file = open(word_dict_path, "rb")
    pickle_bytes = pickle_file.read()
    word_dict = pickle.loads(pickle_bytes)
    return word_dict


def read_or_create_word_dict(doc_path, dict_path, name, force=False, with_tags=False):
    print("read_or_create_word_dict:", locals())
    word_dict_path = os.path.join(dict_path, f'word_dict.{name}')
    if not force and os.path.exists(word_dict_path):
        return read_word_dict(word_dict_path)
    else:
        word_dict, tags_dict = create_word_and_tags_dict(doc_path)
        word_tags_dict = merge_dict2_into_dict1(word_dict, tags_dict) if with_tags else word_dict
        pickle_file = open_file_for_writing_with_path_creation(word_dict_path, 'wb')
        pickle.dump(word_tags_dict, pickle_file)
        return word_dict
