import os
import json

from gensim import corpora, models

from python.words.words_of_file import create_words_dict
from python.tfidf import create_tfidf_files
from python.get_args import get_args, get_int_env_var, get_str_env_var, NUM_TOPICS, OUT_SUB_FOLDER
from python.util.util import open_file_for_writing_with_path_creation


def create_vectors(word_dict: dict, out_path: str, num_topics: int, tfidf_suffix = "tfidf2.csv", vectors_file_name = "vectors2.csv"):
    print("---- create word dict ----")
    only_long_words = {file_path: list(filter(lambda w: len(w) > 2, word_dict[file_path].split(' '))) for file_path in list(word_dict.keys())}
    documents = list(only_long_words.values())
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    print("--- create lsi model ----")
    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    for doc_no in range(len(corpus_tfidf)):
        file_name = f"{list(only_long_words.keys())[doc_no]}.{tfidf_suffix}"
        print(f"create: {file_name}")
        tfidf_abs_path = os.path.join(out_path, "tfidf", file_name)
        if not os.path.exists(tfidf_abs_path):
            tfidf_file = open_file_for_writing_with_path_creation(tfidf_abs_path)
            for tupel_no in range(len(corpus_tfidf[doc_no])):
                print(f"{dictionary[corpus_tfidf[doc_no][tupel_no][0]].strip()}\t{corpus_tfidf[doc_no][tupel_no][1]}", file=tfidf_file)

    vectors_out_path = f"{out_path}/{vectors_file_name}"

    if not os.path.exists(vectors_out_path):
        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)

        vectors_out_file = open_file_for_writing_with_path_creation(vectors_out_path)

        print("---- create vectors ----")
        only_many_words = {file_path: only_long_words[file_path] for file_path in list(filter(lambda k: len(only_long_words[k]) > 20, only_long_words.keys()))}
        for i, file_rel_path in enumerate(only_many_words.keys()):
            vectors_out_list = [file_rel_path]
            vec_bow = dictionary.doc2bow(only_many_words[file_rel_path])
            vec_lsi = lsi[vec_bow]

            for entry in vec_lsi:
                vectors_out_list.append(str(round(entry[1], 2)))

            print("\t".join(vectors_out_list), file=vectors_out_file)

            if i%100 == 0:
                print(i)


def main():
    args = get_args(doc_path_required=True, out_path_required=True)
    out_sub_folder = get_str_env_var(OUT_SUB_FOLDER, "")
    out_path = os.path.join(args.outpath, out_sub_folder)
    word_dict, all_word_dict = create_words_dict(doc_path=args.docpath, out_path=out_path)
    num_topics = get_int_env_var(NUM_TOPICS, 200)
    create_tfidf_files(word_dict, out_path=out_path, num_topics=num_topics)

    create_vectors(word_dict, out_path=out_path, num_topics=num_topics)
    create_vectors(all_word_dict, out_path=out_path, num_topics=num_topics, tfidf_suffix="tfidf_all.csv", vectors_file_name="vectors_all.csv")


if __name__ == "__main__":
    main()
