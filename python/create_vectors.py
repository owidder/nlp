import os
import json

from gensim import corpora, models

from words.words_of_file import create_word_and_tags_dict
from python.tfidf import find_features
from get_args import get_args, get_int_env_var, get_str_env_var, get_bool_env_var, NUM_TOPICS, OUT_SUB_FOLDER, CLASSIC_MODE, STOPWORDS_PATH
from util.util import open_file_for_writing_with_path_creation


def create_vectors(word_dict: dict, out_path: str, num_topis: int):
    print("---- create word dict ----")
    documents = [word.split(' ') for word in list(word_dict.values())]
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    print("--- create lsi model ----")
    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topis)

    vectors_out_file = open_file_for_writing_with_path_creation(f"{out_path}/vectors.csv")

    print("---- create vectors ----")
    for i, file_rel_path in enumerate(word_dict.keys()):
        vectors_out_list = [file_rel_path]
        content = word_dict[file_rel_path]
        vec_bow = dictionary.doc2bow(content.split())
        vec_lsi = lsi[vec_bow]

        for entry in vec_lsi:
            vectors_out_list.append(str(round(entry[1], 2)))

        print("\t".join(vectors_out_list), file=vectors_out_file)

        if i%100 == 0:
            print(i)


def create_word_dict(doc_path):
    return create_word_and_tags_dict(doc_path=doc_path)[0]


def main():
    stopwords = {}
    stopwords_path = get_str_env_var(STOPWORDS_PATH, "")
    if len(stopwords_path) > 0:
        stopwordsFile = open(stopwords_path)
        stopwords = json.load(stopwordsFile)

    args = get_args(doc_path_required=True, out_path_required=True)
    out_sub_folder = get_str_env_var(OUT_SUB_FOLDER, "")
    out_path = os.path.join(args.outpath, out_sub_folder)
    word_dict = create_word_and_tags_dict(doc_path=args.docpath, out_path=out_path, stopwords=stopwords)[0]
    num_topics = get_int_env_var(NUM_TOPICS, 200)
    tfidf_word_dict = find_features(word_dict, doc_path=args.docpath, out_path=os.path.join(out_path, "tfidf"))

    if get_bool_env_var(CLASSIC_MODE, False):
        create_vectors(word_dict, out_path=out_path, num_topis=num_topics)
    else:
        create_vectors(tfidf_word_dict, out_path=out_path, num_topis=num_topics)


if __name__ == "__main__":
    main()
