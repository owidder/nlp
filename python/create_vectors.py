import os
import argparse

from gensim import corpora, models

from python.words.words_of_file import create_words_dict
from python.tfidf import create_tfidf_files
from python.util.util import open_file_for_writing_with_path_creation
from python.aggregate import aggregate_folder


def create_vectors(word_dict: dict, out_path: str, num_topics: int, vectors_file_name = "vectors2.csv"):
    print("---- create word dict ----")
    only_long_words = {file_path: list(filter(lambda w: len(w) > 2, word_dict[file_path].split(' '))) for file_path in list(word_dict.keys())}
    documents = list(only_long_words.values())
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    print("--- create lsi model ----")
    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    vectors_out_path = f"{out_path}/{vectors_file_name}"

    if not os.path.exists(vectors_out_path):
        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)

        vectors_out_file = open_file_for_writing_with_path_creation(vectors_out_path)

        print("---- create vectors ----")
        only_many_words = {file_path: only_long_words[file_path] for file_path in list(filter(lambda k: len(only_long_words[k]) > 1, only_long_words.keys()))}
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--docpath', required=True, action='store', help='Path to the documents')
    parser.add_argument('--outpath', required=True, action='store', help='Path to the output folder')
    args = parser.parse_args()

    word_dict = create_words_dict(doc_path=args.docpath, out_path=args.outpath)
    create_tfidf_files(word_dict, out_path=args.outpath)
    create_vectors(word_dict, out_path=args.outpath, num_topics=2000)
    aggregate_folder(folder_path=args.outpath)


if __name__ == "__main__":
    main()
