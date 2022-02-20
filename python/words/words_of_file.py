import os
import pickle
import re
import sys
import traceback
import json

import enchant
import nltk
import ssl
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from python.util.util import rel_path_from_abs_path, open_file_for_writing_with_path_creation
from python.util.dict_util import merge_dict2_into_dict1
from python.get_args import get_bool_env_var, get_int_env_var, get_str_env_var, \
    WITH_STEMMING, DO_REMOVE_NON_CHARS, MIN_WORD_SIZE, DO_REMOVE_STOP_WORDS, DO_FILTER_NON_EN_DE_WORDS, DO_SPLIT_CAMEL_CASE, \
    USE_ANTLR, INCLUDE_FOLDERS
from python.antlr.extract_essential_words_from_python import extract_essential_words_from_python
from python.antlr.extract_essential_words_from_java import extract_essential_words_from_java
from python.antlr.antlrCaller import callAntlr

from typing import List

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


def filter_min_word_size(string, min_word_size):
    return ' '.join([w for w in string.split() if len(w) >= min_word_size])


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


_unstem_dict = None

def add_to_unstem_dict(word: str, stemmed_word: str, unstem_dict: {}):
    if stemmed_word in unstem_dict:
        if len(word) < len(unstem_dict[stemmed_word]):
            unstem_dict[stemmed_word] = word
    else:
        unstem_dict[stemmed_word] = word


def stemming(data: str, unstem_dict: {}):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for word in tokens:
        stemmed_word = stemmer.stem(word)
        add_to_unstem_dict(word, stemmed_word, unstem_dict)
        new_text = new_text + " " + stemmer.stem(word)

    return new_text


def  is_en_de(word):
    result = en.check(word) or de.check(word)
    return result


def filter_non_en_de_words(data):
    tokens = word_tokenize(str(data))
    return " ".join(list(filter(lambda word: is_en_de(word), tokens)))


def process_words(text, unstem_dict: {}, with_stemming=None,
                  do_remove_non_chars=False,
                  do_split_camel_case=False,
                  do_remove_stop_words=False,
                  do_filter_non_en_de_words=False,
                  min_word_size=0):
    words_of_file = re.sub('[^A-Za-z ]+', ' ', text) if get_bool_env_var(DO_REMOVE_NON_CHARS, do_remove_non_chars) else text
    words_of_file = split_camel_case(words_of_file) if get_bool_env_var(DO_SPLIT_CAMEL_CASE, do_split_camel_case) else words_of_file
    _min_word_size = get_int_env_var(MIN_WORD_SIZE, min_word_size)
    words_of_file = filter_min_word_size(words_of_file, min_word_size=_min_word_size) if _min_word_size > 0 else words_of_file
    words_of_file = remove_stop_words(words_of_file) if get_bool_env_var(DO_REMOVE_STOP_WORDS, do_remove_stop_words) else words_of_file
    words_of_file = filter_non_en_de_words(words_of_file) if get_bool_env_var(DO_FILTER_NON_EN_DE_WORDS, do_filter_non_en_de_words) else words_of_file
    words_of_file = stemming(words_of_file, unstem_dict) if get_bool_env_var(WITH_STEMMING, with_stemming) else words_of_file
    words_of_file = words_of_file.lower()
    return words_of_file


def parse_important_words(file_path: str, unstem_dict: {}):
    try:
        extension = file_path.split(".")[-1]
        if extension in ["js", "jsx", "ts", "tsx", "php"]:
            essential_words = callAntlr(file_path)
        elif extension == "py":
            essential_words = extract_essential_words_from_python(open(file_path, 'r').read())
        elif extension == "java":
            essential_words = extract_essential_words_from_java(open(file_path, 'r').read())
        else:
            essential_words = open(file_path, 'r').read()

        filename_with_extension = file_path.split(os.path.sep)[-1]
        filename_without_extension = filename_with_extension.split(".")[0]
        essential_words = " ".join([essential_words, filename_without_extension])
        wof = process_words(essential_words, unstem_dict=unstem_dict)
        print(wof)
        print("----------------------------------------------")
        return wof
    except:
        print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        traceback.print_exc(file=sys.stdout)
        return ""


def is_no_dot_file(file_path):
    return len(list(filter(lambda part: part.startswith("."), file_path.split("/")))) == 0


def has_included_extension(file_path):
    parts = file_path.split(".")
    if len(parts) > 1:
        return parts[-1].lower() in ["py", "js", "json", "txt", "md", "html", "jsx", "ts", "tsx", "java", "php"]
    return False


def is_included(file_path, include_folders: []):
    _is_included = is_no_dot_file(file_path) and has_included_extension(file_path)

    for include_folder in include_folders:
        if file_path.find(include_folder) > -1:
            return _is_included

    return False


def unstem(word_stemmed, unstem_dict):
    print(f"unstem\t{word_stemmed}\t{unstem_dict[word_stemmed]}")
    return unstem_dict[word_stemmed]


def is_stopword(current_path: str, stopword_path: str, word: str, stopwords: List[str]):
    if stopword_path == "." or current_path.startswith(stopword_path):
        return word in stopwords

    return False


def filter_stopwords(rel_path: str, words: str, stopwords: {}) -> str:
    wordArray = words.split(" ")
    for _path in stopwords:
        wordArray = [word for word in wordArray if not is_stopword(rel_path, _path, word, stopwords[_path])]

    return " ".join(wordArray)


def unstem_word_dict(word_dict_stemmed, unstem_dict):
    return {file_rel_path: " ".join([unstem(word_stemmed, unstem_dict) for word_stemmed in words_stemmed.split()]) for file_rel_path, words_stemmed in word_dict_stemmed.items()}


def read_or_create_unstem_dict(out_path: str) -> dict:
    unstem_dict_path = os.path.join(out_path, "unstem_dict.json")
    return json.loads(open(unstem_dict_path, "r").read()) if os.path.isfile(unstem_dict_path) else {}


def write_unstem_dict(out_path: str, unstem_dict: dict):
    unstem_dict_str = json.dumps(unstem_dict)
    unstem_dict_file = open_file_for_writing_with_path_creation(os.path.join(out_path, "unstem_dict.json"), "w")
    unstem_dict_file.write(unstem_dict_str)
    unstem_dict_file.close()


def create_words_dict(doc_path, out_path, stopwords) -> dict:
    print("create_word_dict:", locals())
    word_dict = {}
    tags_dict = {}
    unstem_dict: dict = read_or_create_unstem_dict(out_path)
    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = subdir + os.path.sep + file
            include_folders = get_str_env_var(INCLUDE_FOLDERS, "").split(",")
            if is_included(file_abs_path, include_folders):
                try:
                    file_rel_path = rel_path_from_abs_path(doc_path, file_abs_path)
                    word_file_path = os.path.join(out_path, "words", f"{file_rel_path}._words_")

                    if os.path.isfile(word_file_path):
                        print(f"read from file: [{word_file_path}] ->")
                        words_of_file = open(word_file_path, "r").read()
                        print(words_of_file)
                        print("--------------------------------------------")
                    else:
                        words_of_file = parse_important_words(file_abs_path, unstem_dict=unstem_dict)
                        write_unstem_dict(out_path, unstem_dict)
                        words_of_file = filter_stopwords(file_rel_path, words_of_file, stopwords)
                        word_file = open_file_for_writing_with_path_creation(word_file_path)
                        print(words_of_file, file=word_file)

                    if len(words_of_file) > 0:
                        word_dict[file_rel_path] = words_of_file
                except:
                    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
                    traceback.print_exc(file=sys.stdout)

    return word_dict


def read_word_dict(word_dict_path):
    pickle_file = open(word_dict_path, "rb")
    pickle_bytes = pickle_file.read()
    word_dict = pickle.loads(pickle_bytes)
    return word_dict
