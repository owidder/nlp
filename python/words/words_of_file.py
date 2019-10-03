from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

import nltk
import re
import string
import enchant

nltk.download('punkt')
nltk.download('stopwords')

unstem_dict = {}

en = enchant.Dict("en_US")
de = enchant.Dict("de_DE")
fr = enchant.Dict("fr_FR")


def split_camel_case(name):
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', name).lower()


def removeSingleChars(string):
    return ' '.join([w for w in string.split() if len(w) > 1])


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
    return unstem_dict[word]


def is_en_de_fr(word):
    return en.check(word) or de.check(word) or fr.check(word)


def filter_non_en_de_fr_words(data):
    tokens = word_tokenize(str(data))
    return " ".join(list(filter(lambda w: is_en_de_fr(unstem(w)), tokens)))


def words_of_file(file_path):
    try:
        shakes = open(file_path, 'r')
        text = shakes.read()
        no_punctuation = text.translate(string.punctuation)
        only_a_to_z = re.sub('[^A-Za-z ]+', ' ', no_punctuation)
        camel_case_split = split_camel_case(only_a_to_z)
        camel_case_split_no_single_chars = removeSingleChars(camel_case_split)
        camel_case_split_no_single_chars_no_stop_words = remove_stop_words(camel_case_split_no_single_chars)
        camel_case_split_no_single_chars_no_stop_words_stemmed = stemming(camel_case_split_no_single_chars_no_stop_words)
        camel_case_split_no_single_chars_no_stop_words_stemmed_only_en_de_fr = filter_non_en_de_fr_words(camel_case_split_no_single_chars_no_stop_words_stemmed)
        return camel_case_split_no_single_chars_no_stop_words_stemmed_only_en_de_fr
    except:
        return ""


