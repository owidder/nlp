import nltk
import os
import argparse

from sklearn.feature_extraction.text import TfidfVectorizer

from words.words_of_file import unstem, get_words_of_file, read_or_create_word_dict, is_included
from util.util import rel_path_from_abs_path, open_file_for_writing_with_path_creation


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def fit(word_dict):
    tfidf = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english')
    print("--- start fit transform ---\n")
    tfidf.fit_transform(word_dict.values())
    print("--- fit transform ended ---\n")
    return tfidf


def find_features(doc_path, word_dict_path, out_path,  name):
    word_dict = read_or_create_word_dict(doc_path=doc_path, word_dict_path=word_dict_path, name=name)

    print("---- do the fitting ----\n")
    tfidf = fit(word_dict)
    feature_names = tfidf.get_feature_names()

    print("--- analyze root path ---\n")
    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = os.path.join(subdir, file)
            if is_included(file_abs_path):
                file_rel_path = rel_path_from_abs_path(base_path=doc_path, abs_path=file_abs_path)
                file_out_path = os.path.join(out_path, f"{file_rel_path}.tfidf.csv")
                print("--> " + file_out_path)
                file_str = word_dict[file_rel_path]
                file_response = tfidf.transform([file_str])

                f = {}
                for col in file_response.nonzero()[1]:
                    f[feature_names[col]] = file_response[0, col]

                if len(list(f.keys())) > 0:
                    out_file = open_file_for_writing_with_path_creation(file_out_path)
                    sf = sorted(f, key=f.__getitem__, reverse=True)
                    for k in sf:
                        uk = unstem(k)
                        print(uk + "\t" + str(f[k]), file=out_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--docpath', required=True, action='store', help='Path to the documents')
    parser.add_argument('--dictpath', required=True, action='store', help='Path to the dictionarty. Has to be name word_dict.<name>.pickle. If it does not exist, it will be created')
    parser.add_argument('--outpath', required=True, action='store', help='Path to the output folder')
    parser.add_argument('--name', required=True, action='store', help='Name of the dictionary (see paramter --dictpath)')

    args = parser.parse_args()

    find_features(doc_path=args.docpath, word_dict_path=args.dictpath, out_path=args.outpath, name=args.name)


if __name__ == "__main__":
    main()
