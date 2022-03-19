import os
import json

from gensim import corpora, models

from python.words.words_of_file import create_words_dict
from python.tfidf import create_tfidf_files
from python.get_args import get_args, get_int_env_var, get_str_env_var, NUM_TOPICS, OUT_SUB_FOLDER
from python.util.util import open_file_for_writing_with_path_creation


def create_vectors(word_dict: dict, out_path: str, num_topis: int):
    print("---- create word dict ----")
    documents = [word.split(' ') for word in list(word_dict.values())]
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    print("--- create lsi model ----")
    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    for doc_no in range(len(corpus_tfidf)):
        file_name = f"{list(word_dict.keys())[doc_no]}.tfidf2.csv"
        print(f"create: {file_name}")
        tfidf_abs_path = os.path.join(out_path, "tfidf", file_name)
        if not os.path.exists(tfidf_abs_path):
            tfidf_file = open_file_for_writing_with_path_creation(tfidf_abs_path)
            for tupel_no in range(len(corpus_tfidf[doc_no])):
                print(f"{dictionary[corpus_tfidf[doc_no][tupel_no][0]].strip()}\t{corpus_tfidf[doc_no][tupel_no][1]}", file=tfidf_file)

    vectors_out_path = f"{out_path}/vectors2.csv"

    if not os.path.exists(vectors_out_path):
        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topis)

        vectors_out_file = open_file_for_writing_with_path_creation(vectors_out_path)

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


def main():
    args = get_args(doc_path_required=True, out_path_required=True)
    out_sub_folder = get_str_env_var(OUT_SUB_FOLDER, "")
    out_path = os.path.join(args.outpath, out_sub_folder)
    word_dict = create_words_dict(doc_path=args.docpath, out_path=out_path)
    num_topics = get_int_env_var(NUM_TOPICS, 200)
    create_tfidf_files(word_dict, out_path=out_path)

    create_vectors(word_dict, out_path=out_path, num_topis=num_topics)


if __name__ == "__main__":
    main()
