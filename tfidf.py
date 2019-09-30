from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

import nltk
import string
import os
import errno
import re
import sys
import numpy as np
import enchant

from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')


en = enchant.Dict("en_US")
de = enchant.Dict("de_DE")
fr = enchant.Dict("fr_FR")

unstem_dict = {}
english_words = []

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def splitCamelCase(name):
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', name).lower()


def removeSingleChars(string):
    return ' '.join([w for w in string.split() if len(w) > 1])


def convert_lower_case(data):
    return np.char.lower(data)


def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text


def add_to_unstem_dict(word, stemmed_word):
    if stemmed_word in unstem_dict:
        if len(word) < len(unstem_dict[stemmed_word]):
            unstem_dict[stemmed_word] = word
    else:
        unstem_dict[stemmed_word] = word


def unstem(word):
    return unstem_dict[word]


def stemming(data):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        stemmed_word = stemmer.stem(w)
        add_to_unstem_dict(w, stemmed_word)
        new_text = new_text + " " + stemmer.stem(w)

    return new_text


def filter_non_english_words(data):
    tokens = word_tokenize(str(data))
    return " ".join(list(filter(lambda w: unstem(w) in english_words, tokens)))


def is_en_de_fr(word):
    return en.check(word) or de.check(word) or fr.check(word)


def filter_non_en_de_fr_words(data):
    tokens = word_tokenize(str(data))
    return " ".join(list(filter(lambda w: is_en_de_fr(unstem(w)), tokens)))


def fileString(file_path):
    try:
        shakes = open(file_path, 'r')
        text = shakes.read()
        no_punctuation = text.translate(string.punctuation)
        only_a_to_z = re.sub('[^A-Za-z ]+', ' ', no_punctuation)
        camel_case_split = splitCamelCase(only_a_to_z)
        camel_case_split_no_single_chars = removeSingleChars(camel_case_split)
        camel_case_split_no_single_chars_no_stop_words = remove_stop_words(camel_case_split_no_single_chars)
        camel_case_split_no_single_chars_no_stop_words_stemmed = stemming(camel_case_split_no_single_chars_no_stop_words)
        camel_case_split_no_single_chars_no_stop_words_stemmed_only_english = filter_non_en_de_fr_words(camel_case_split_no_single_chars_no_stop_words_stemmed)
        return camel_case_split_no_single_chars_no_stop_words_stemmed_only_english
    except:
        return ""


def isNoDotFile(file_path):
    return len(list(filter(lambda part: part.startswith("."), file_path.split("/")))) == 0


def hasNoExcludedExtension(file_path):
  extension = file_path.split(".")[-1]
  return extension.lower() not in ["jpg", "jpeg", "png", "bmp", "csv"]


def isIncluded(file_path):
    return isNoDotFile(file_path) and hasNoExcludedExtension(file_path)


def relPathFromAbsPath(rootPath, absPath):
  return re.sub(rootPath + "/", '', absPath)


def tokenizePath(path):
    token_dict = {}
    for subdir, dirs, files in os.walk(path):
        for file in files:
            file_path = subdir + os.path.sep + file
            if isIncluded(file_path):
                wordsOfFile = fileString(file_path)
                if len(wordsOfFile) > 0:
                    token_dict[file] = wordsOfFile
    return token_dict


def fit(corpusPath):
    token_dict = tokenizePath(corpusPath)
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    print("--- start fit transform ---\n")
    tfidf.fit_transform(token_dict.values())
    print("--- fit transform ended ---\n")
    return tfidf


def openFileForWritingWithPathCreation(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return open(file_path, 'w')


def readEnglishWords():
    global english_words
    english_words = [line.rstrip('\n') for line in open("./english-words/corncob_lowercase.txt").readlines()]


def findFeatures(corpusPath, rootPath):
    print("---- do the fitting ----\n")
    tfidf = fit(corpusPath=corpusPath)
    print("--- analyze root path ---\n")
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            file_path = subdir + os.path.sep + file
            if isIncluded(file_path):
                out_file_path = "out/" + relPathFromAbsPath(rootPath, file_path) + ".tfidf.csv"
                print("--> " + out_file_path)
                file_str = fileString(file_path)
                file_response = tfidf.transform([file_str])
                feature_names = tfidf.get_feature_names()

                f = {}
                for col in file_response.nonzero()[1]:
                    f[feature_names[col]] = file_response[0, col]

                if len(list(f.keys())) > 0:
                    out_file = openFileForWritingWithPathCreation(out_file_path)
                    sf = sorted(f, key=f.__getitem__, reverse=True)
                    for k in sf:
                        uk = unstem(k)
                        print(uk + "\t" + str(f[k]), file=out_file)


corpusPath = sys.argv[1]
rootPath = (sys.argv[2] if len(sys.argv) > 2 else corpusPath)

readEnglishWords()

findFeatures(corpusPath=corpusPath, rootPath=rootPath)
