import os

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

from util.util import rel_path_from_abs_path, open_file_for_writing_with_path_creation
from words.words_of_file import is_included
from get_args import get_int_env_var, get_float_env_var, MAX_WORDS, MIN_TFIDF


def fit(word_dict):
    tfidf = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english', lowercase=False)
    print("--- start fit transform ---\n")
    tfidf.fit_transform(word_dict.values())
    print("--- fit transform ended ---\n")
    return tfidf


def find_features(word_dict: dict, doc_path: str, out_path: str) -> dict:
    tfidf_word_dict = {}
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
                try:
                    file_str = word_dict[file_rel_path]
                    file_response = tfidf.transform([file_str])

                    f = {}
                    for col in file_response.nonzero()[1]:
                        f[feature_names[col]] = file_response[0, col]

                    if len(list(f.keys())) > 0:
                        out_file = open_file_for_writing_with_path_creation(file_out_path)
                        sf = sorted(f, key=f.__getitem__, reverse=True)
                        max_words = get_int_env_var(MAX_WORDS, 0)
                        if max_words > 0:
                            fsf = sf[:max_words]
                        else:
                            min_tfidf = get_float_env_var(MIN_TFIDF, 0.0)
                            fsf = [k for k in sf if f[k] > min_tfidf]

                        tfidf_word_dict[file_rel_path] = ' '.join(fsf)
                        for k in fsf:
                            print(f"{k}\t{str(f[k])}", file=out_file)
                except:
                    print(f"Couldn't find {file_rel_path}")

    return tfidf_word_dict

