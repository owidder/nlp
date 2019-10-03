import os

from ..words.words_of_file import words_of_file

def is_no_dot_file(file_path):
    return len(list(filter(lambda part: part.startswith("."), file_path.split("/")))) == 0


def has_no_excluded_extension(file_path):
    extension = file_path.split(".")[-1]
    return extension.lower() not in ["jpg", "jpeg", "png", "bmp", "csv"]


def is_included(file_path):
    return is_no_dot_file(file_path) and has_no_excluded_extension(file_path)


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
