import os
import re
import sys
import traceback
import json
from subprocess import check_output
import multiprocessing as mp

import nltk
import ssl
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from python.util.util import rel_path_from_abs_path, open_file_for_writing_with_path_creation
from python.antlr.extract_essential_phrases_from_python_with_strings import extract_essential_phrases_from_python
from python.antlr.extract_essential_phrases_from_java_with_strings import extract_essential_phrases_from_java

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')

global_unstem_dict: dict = {}
global_log_counter: dict[str, int] = {}

stemmer = PorterStemmer()


def init_global_unstem_dict(out_path: str):
    global global_unstem_dict
    unstem_dict_path = os.path.join(out_path, "unstem_dict.json")
    if(os.path.isfile(unstem_dict_path)):
        global_unstem_dict = json.loads(open(unstem_dict_path, "r").read())


def add_to_global_unstem_dict(term: str, stemmed_term: str):
    global global_unstem_dict
    if stemmed_term in global_unstem_dict:
        if not term in global_unstem_dict[stemmed_term]:
            global_unstem_dict[stemmed_term].append(term)
    else:
        global_unstem_dict[stemmed_term] = [term]


def stem(term: str):
    stemmed_term = stemmer.stem(term)
    add_to_global_unstem_dict(term, stemmed_term)
    return stemmed_term.lower()


def extract_essential_terms(file_path: str, doStem = True) -> [str]:
    try:
        # we do not need files with super long lines, because they are most probably semi-binary (e.g. js bundles)
        if os.path.getsize(file_path) == 0 or len(max(open(file_path, "r"), key=len)) > 500:
            return []

        extension: str = file_path.split(".")[-1].lower()
        if extension in ["js", "jsx", "ts", "tsx"]:
            path_to_jar = os.getenv("PATH_TO_JAR", "bin/antlr-1.0-SNAPSHOT.jar")
            abs_path_to_jar = os.path.abspath(path_to_jar)
            essential_phrases = word_tokenize(check_output(["java", "-jar", abs_path_to_jar, file_path]).decode("utf-8"))
        elif extension == "py":
            essential_phrases = extract_essential_phrases_from_python(open(file_path, 'r').read())
        elif extension == "java":
            essential_phrases = extract_essential_phrases_from_java(open(file_path, 'r').read())
        else:
            return []

        essential_phrases = [re.sub('^(.*)$', r' \1 ', phrase) for phrase in essential_phrases] # insert space at beginning and end of line
        essential_phrases = [re.sub('[^A-Za-z ]+', ' ', phrase) for phrase in essential_phrases] # remove all non chars
        essential_phrases = [re.sub('([a-z])([A-Z])', r'\1 \2', phrase) for phrase in essential_phrases] # split camel case
        essential_phrases = [re.sub('(?<= )([A-Z]+)([A-Z][a-z]+)(?= )', r'\2', phrase) for phrase in essential_phrases] # remove more than one cap at beginning of word
        essential_terms: [str] = [term for term_list in [word_tokenize(phrase) for phrase in essential_phrases] for term in term_list]


        return [stem(term.lower()) if doStem else term.lower() for term in essential_terms]
    except:
        print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        traceback.print_exc(file=sys.stdout)
        return []


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


def is_included(file_path):
    return is_no_dot_file(file_path) and has_included_extension(file_path)


def write_unstem_dict(out_path: str, unstem_dict: dict):
    unstem_dict_str = json.dumps(unstem_dict)
    unstem_dict_file = open_file_for_writing_with_path_creation(os.path.join(out_path, "unstem_dict.json"), "w")
    unstem_dict_file.write(unstem_dict_str)
    unstem_dict_file.close()


def log_count(file_path: str):
    global global_log_counter
    extension: str = file_path.split(".")[-1].lower()

    count = global_log_counter.get(extension, 0)
    count += 1
    global_log_counter[extension] = count

    print(f"{extension}: {global_log_counter[extension]}")


def write_one_long_words_file(file_abs_path: str, essential_long_words_file_path: str) -> str:
    print(f"create: {essential_long_words_file_path}")
    essential_long_terms = extract_essential_terms(file_abs_path, False)
    essential_long_words_str = " ".join(essential_long_terms)
    print(essential_long_words_str, file=open_file_for_writing_with_path_creation(essential_long_words_file_path))

    return "OK"


def write_long_words_files_parallel(doc_path: str, out_path: str):
    pool = mp.Pool(mp.cpu_count())

    results = []

    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = subdir + os.path.sep + file
            if is_included(file_abs_path):
                try:
                    file_rel_path = rel_path_from_abs_path(doc_path, file_abs_path)

                    essential_long_words_file_path = os.path.join(out_path, "words", f"{file_rel_path}._long_words_")
                    if not os.path.isfile(essential_long_words_file_path):
                        results.append(pool.apply_async(write_one_long_words_file, (file_abs_path, essential_long_words_file_path,)))

                except:
                    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
                    traceback.print_exc(file=sys.stdout)

    print(filter(lambda r: r != "OK", [result.get() for result in results]))


def create_words_dict(doc_path, out_path):
    print("create_word_dict:", locals())
    word_dict = {}
    init_global_unstem_dict(out_path)
    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = subdir + os.path.sep + file
            print(f"--> {file_abs_path}")
            if is_included(file_abs_path):
                try:
                    file_rel_path = rel_path_from_abs_path(doc_path, file_abs_path)

                    log_count(file_abs_path)

                    essential_words_file_path = os.path.join(out_path, "words", f"{file_rel_path}._words_")
                    essential_words_str = ""
                    if os.path.isfile(essential_words_file_path):
                        print(f"read from file: <{essential_words_file_path}> ->")
                        essential_words_str = open(essential_words_file_path, "r").read()
                        print("--------------------------------------------")
                    else:
                        essential_long_words_file_path = os.path.join(out_path, "words", f"{file_rel_path}._long_words_")
                        if os.path.isfile(essential_long_words_file_path):
                            essential_long_words_str = open(essential_long_words_file_path, "r").read()
                            essential_terms = [stem(word) for word in word_tokenize(essential_long_words_str)]
                        else:
                            essential_terms  = extract_essential_terms(file_abs_path)

                        essential_words_str = " ".join(essential_terms)
                        print(essential_words_str, file=open_file_for_writing_with_path_creation(essential_words_file_path))
                        if len(essential_terms) > 0:
                            write_unstem_dict(out_path, global_unstem_dict)

                        print("--------------------------------------------")

                    if len(essential_words_str) > 0:
                        word_dict[file_rel_path] = essential_words_str

                except:
                    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
                    traceback.print_exc(file=sys.stdout)

    print(f"number of files = {len(word_dict.keys())}")
    return word_dict
