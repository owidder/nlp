import logging
from gensim import corpora
from collections import defaultdict
import os
import pickle
import argparse

from words.words_of_file import read_or_create_word_unstem_dict, is_included


def create_corpus(doc_path, word_dict_path, name, out_path):
    word_unstem_dict = read_or_create_word_unstem_dict(doc_path=doc_path, dict_path=word_dict_path, name=name)
    texts = [[word for word in document.lower().split()] for document in list(word_unstem_dict.word_dict.values())]
    # remove words that appear only once
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]
    dictionary = corpora.Dictionary(texts)
    dictionary.save(f"{out_path}/corpus-{name}.dict")
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(f"{out_path}/corpus-{name}.mm", corpus)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--docpath', required=True, action='store', help='Path to the documents')
    parser.add_argument('--dictpath', required=True, action='store', help='Path to the dictionarty. Has to be name word_dict.<name>.pickle. If it does not exist, it will be created')
    parser.add_argument('--outpath', required=True, action='store', help='Path to the output folder')
    parser.add_argument('--name', required=True, action='store', help='Name of the dictionary (see paramter --dictpath)')

    args = parser.parse_args()

    create_corpus(doc_path=args.docpath, word_dict_path=args.dictpath, out_path=args.outpath, name=args.name)


if __name__ == "__main__":
    main()
