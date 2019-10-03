import nltk
import os
import errno
import re
import sys

from sklearn.feature_extraction.text import TfidfVectorizer

from util.words_of_file import words_of_file, unstem

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
                wordsOfFile = words_of_file(file_path)
                if len(wordsOfFile) > 0:
                    token_dict[file] = wordsOfFile
    return token_dict


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens


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
                file_str = words_of_file(file_path)
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

def main():
    corpusPath = sys.argv[1]
    rootPath = (sys.argv[2] if len(sys.argv) > 2 else corpusPath)

    findFeatures(corpusPath=corpusPath, rootPath=rootPath)


if __name__ == "__main__":
    main()
    