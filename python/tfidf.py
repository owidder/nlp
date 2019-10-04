import nltk
import os
import errno
import re
import sys

from sklearn.feature_extraction.text import TfidfVectorizer

from words.words_of_file import unstem, get_words_of_file, create_word_dict, is_included


def rel_path_from_abs_path(rootPath, absPath):
    return re.sub(rootPath + "/", '', absPath)


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def fit(corpusPath):
    word_dict = create_word_dict(corpusPath)
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    print("--- start fit transform ---\n")
    tfidf.fit_transform(word_dict.values())
    print("--- fit transform ended ---\n")
    return tfidf


def open_file_for_writing_with_path_creation(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return open(file_path, 'w')


def find_features(corpusPath, rootPath):
    print("---- do the fitting ----\n")
    tfidf = fit(corpusPath=corpusPath)
    print("--- analyze root path ---\n")
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            file_path = subdir + os.path.sep + file
            if is_included(file_path):
                out_file_path = "out/" + rel_path_from_abs_path(rootPath, file_path) + ".tfidf.csv"
                print("--> " + out_file_path)
                file_str = get_words_of_file(file_path)
                file_response = tfidf.transform([file_str])
                feature_names = tfidf.get_feature_names()

                f = {}
                for col in file_response.nonzero()[1]:
                    f[feature_names[col]] = file_response[0, col]

                if len(list(f.keys())) > 0:
                    out_file = open_file_for_writing_with_path_creation(out_file_path)
                    sf = sorted(f, key=f.__getitem__, reverse=True)
                    for k in sf:
                        uk = unstem(k)
                        print(uk + "\t" + str(f[k]), file=out_file)


def main():
    corpus_path = sys.argv[1]
    root_path = (sys.argv[2] if len(sys.argv) > 2 else corpus_path)

    find_features(corpusPath=corpus_path, rootPath=root_path)


if __name__ == "__main__":
    main()
