import sys
import argparse

from words.words_of_file import read_or_create_word_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--docpath', required=True, action='store', help='Path to the documents')
    parser.add_argument('--dictpath', required=True, action='store', help='Path to the dictionarty. Has to be name word_dict.<name>.pickle. If it does not exist, it will be created')
    parser.add_argument('--name', required=True, action='store', help='Name of the dictionary (see paramter --dictpath)')
    args = parser.parse_args()

    word_dict = read_or_create_word_dict(doc_path=args.docpath, word_dict_path=args.dictpath, name=args.name)
    print(word_dict.keys())


