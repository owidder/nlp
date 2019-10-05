import sys

from words.words_of_file import read_or_create_word_dict

if __name__ == '__main__':
    read_or_create_word_dict(sys.argv[1], sys.argv[2])


