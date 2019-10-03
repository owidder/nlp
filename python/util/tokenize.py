import os

from ..words.words_of_file import words_of_file

def isNoDotFile(file_path):
    return len(list(filter(lambda part: part.startswith("."), file_path.split("/")))) == 0


def hasNoExcludedExtension(file_path):
  extension = file_path.split(".")[-1]
  return extension.lower() not in ["jpg", "jpeg", "png", "bmp", "csv"]


def is_included(file_path):
    return isNoDotFile(file_path) and hasNoExcludedExtension(file_path)


def tokenize_path(path):
    token_dict = {}
    for subdir, dirs, files in os.walk(path):
        for file in files:
            file_path = subdir + os.path.sep + file
            if is_included(file_path):
                wordsOfFile = words_of_file(file_path)
                if len(wordsOfFile) > 0:
                    token_dict[file] = wordsOfFile
    return token_dict
