import os
import re
import sys
import traceback
import json
from subprocess import check_output

import enchant
import nltk
import ssl
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from python.util.util import rel_path_from_abs_path, open_file_for_writing_with_path_creation
from python.get_args import get_str_env_var, INCLUDE_FOLDERS, EXCLUDE_FOLDERS
from python.antlr.extract_essential_phrases_from_python import extract_essential_phrases_from_python
from python.antlr.extract_essential_phrases_from_java import extract_essential_phrases_from_java

from typing import List

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


nltk.download('punkt')


en = enchant.Dict("en_US")
de = enchant.Dict("de_DE")


global_unstem_dict: dict = {}


def init_global_unstem_dict(out_path: str):
    global global_unstem_dict
    unstem_dict_path = os.path.join(out_path, "unstem_dict.json")
    if(os.path.isfile(unstem_dict_path)):
        global_unstem_dict = json.loads(open(unstem_dict_path, "r").read())


def add_to_global_unstem_dict(term: str, stemmed_term: str):
    global global_unstem_dict
    if stemmed_term in global_unstem_dict:
        if len(term) > len(global_unstem_dict[stemmed_term]):
            global_unstem_dict[stemmed_term] = term
    else:
        global_unstem_dict[stemmed_term] = term


def split_camel_case(name):
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', name)


def filter_min_word_size(string, min_word_size):
    return ' '.join([w for w in string.split() if len(w) >= min_word_size])


def stemming(data: str):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for word in tokens:
        stemmed_word = stemmer.stem(word)
        add_to_global_unstem_dict(word, stemmed_word)
        new_text = new_text + " " + stemmer.stem(word)

    return new_text


def  is_en_de(word):
    result = en.check(word) or de.check(word)
    return result


def filter_non_en_de_words(data):
    tokens = word_tokenize(str(data))
    return " ".join(list(filter(lambda word: is_en_de(word), tokens)))


def extract_essential_terms(file_path: str) -> [str]:
    try:
        if os.path.getsize(file_path) == 0 or len(max(open(file_path, "r"), key=len)) > 500:
            return []

        extension: str = file_path.split(".")[-1].lower()
        if extension in ["js", "jsx", "ts", "tsx"]:
            essential_phrases = word_tokenize(check_output(["java", "-jar", os.environ["PATH_TO_JAR"], file_path]).decode("utf-8"))
        elif extension == "py":
            essential_phrases = extract_essential_phrases_from_python(open(file_path, 'r').read())
        elif extension == "java":
            essential_phrases = extract_essential_phrases_from_java(open(file_path, 'r').read())
        else:
            essential_phrases = word_tokenize(open(file_path, 'r').read())

        essential_phrases = [re.sub('^(.*)$', r' \1 ', phrase) for phrase in essential_phrases] # insert space at beginning and end of line
        essential_phrases = [re.sub('[^A-Za-z ]+', ' ', phrase) for phrase in essential_phrases] # remove all non chars
        essential_phrases = [re.sub('([a-z])([A-Z])', r'\1 \2', phrase) for phrase in essential_phrases] # split camel case
        essential_phrases = [re.sub('(?<= )([A-Z]+)([A-Z][a-z]+)(?= )', r'\2', phrase) for phrase in essential_phrases] # remove more than one cap at beginning of word
        essential_terms: [str] = [term for term_list in [word_tokenize(phrase) for phrase in essential_phrases] for term in term_list]

        stemmer = PorterStemmer()

        def stem(term: str):
            stemmed_term = stemmer.stem(term)
            add_to_global_unstem_dict(term, stemmed_term)
            return stemmed_term.lower()

        return [stem(term) for term in essential_terms]
    except:
        print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        traceback.print_exc(file=sys.stdout)
        return ""


def extract_all_terms(file_path: str) -> [str]:
    try:
        if os.path.getsize(file_path) == 0 or len(max(open(file_path, "r"), key=len)) > 500:
            return []

        contents = open(file_path, 'r').read()

        all_terms = re.sub('[^A-Za-z ]+', ' ', contents).split(' ') # remove all non chars
        all_terms = [re.sub('([a-z])([A-Z])', r'\1 \2', term).split() for term in all_terms] # split camel case
        all_terms = [term for term_list in all_terms for term in term_list]

        stemmer = PorterStemmer()

        def stem(term: str):
            stemmed_term = stemmer.stem(term)
            add_to_global_unstem_dict(term, stemmed_term)
            return stemmed_term.lower()

        return [stem(term) for term in all_terms]
    except:
        print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        traceback.print_exc(file=sys.stdout)
        return ""


def is_no_dot_file(file_path):
    return len(list(filter(lambda part: part.startswith("."), file_path.split("/")))) == 0


def has_included_extension(file_path):
    parts = file_path.split(".")
    if len(parts) > 1:
        return parts[-1].lower() in ["py", "js", "jsx", "ts", "tsx", "java"]
    return False


def is_in_excluded_path(file_path: str) -> bool:
    if file_path.find("/static/") > -1:
        return True

    if file_path.find("/lib/") > -1:
        return True

    return False


def is_in_excluded_folder(file_path: str, exclude_folders: [str]) -> bool:
    parts: [str] = file_path.split(os.sep)
    return len(list(filter(lambda part: part in exclude_folders, parts))) > 0


def is_included(file_path, include_folders: [str], exclude_folders: [str]):
    _is_included = is_no_dot_file(file_path) and has_included_extension(file_path) and not is_in_excluded_folder(file_path, exclude_folders)

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


def remove_duplicates(word_str: str) -> str:
    return " ".join(set(word_tokenize(word_str)))


def create_words_dict(doc_path, out_path):
    print("create_word_dict:", locals())
    word_dict = {}
    all_word_dict = {}
    tags_dict = {}
    init_global_unstem_dict(out_path)
    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = subdir + os.path.sep + file
            print(f"--> {file_abs_path}")
            include_folders = get_str_env_var(INCLUDE_FOLDERS, "").split(",")
            exclude_folders = get_str_env_var(EXCLUDE_FOLDERS, "")
            if is_included(file_abs_path, include_folders, exclude_folders.split(",") if len(exclude_folders) > 0 else []):
                try:
                    file_rel_path = rel_path_from_abs_path(doc_path, file_abs_path)

                    essential_words_file_path = os.path.join(out_path, "words", f"{file_rel_path}._words_")
                    essential_words_str = ""
                    if os.path.isfile(essential_words_file_path):
                        print(f"read from file: <{essential_words_file_path}> ->")
                        essential_words_str = open(essential_words_file_path, "r").read()
                        print("--------------------------------------------")
                    else:
                        essential_terms: [str] = extract_essential_terms(file_abs_path)
                        essential_words_str = " ".join(essential_terms)
                        print(essential_words_str, file=open_file_for_writing_with_path_creation(essential_words_file_path))
                        if len(essential_terms) > 0:
                            write_unstem_dict(out_path, global_unstem_dict)

                        print("--------------------------------------------")

                    if len(essential_words_str) > 0:
                        word_dict[file_rel_path] = essential_words_str

                    # all_words_file_path = os.path.join(out_path, "words", f"{file_rel_path}._all_words_")
                    # all_words_str = ""
                    # if os.path.isfile(all_words_file_path):
                    #     print(f"read from file: [{all_words_file_path}] ->")
                    #     all_words_str = open(all_words_file_path, "r").read()
                    #     print(all_words_str)
                    #     print("--------------------------------------------")
                    # else:
                    #     all_terms: [str] = extract_all_terms(file_abs_path)
                    #     if len(all_terms) > 0:
                    #         write_unstem_dict(out_path, global_unstem_dict)
                    #         all_words_str = " ".join(all_terms)
                    #         print(f"{all_words_str}")
                    #         print(all_words_str, file=open_file_for_writing_with_path_creation(all_words_file_path))
                    #
                    #     print("--------------------------------------------")
                    #
                    # if len(all_words_str) > 0:
                    #     all_word_dict[file_rel_path] = all_words_str

                except:
                    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
                    traceback.print_exc(file=sys.stdout)

    print(f"number of files = {len(word_dict.keys())}")
    return word_dict, all_word_dict
