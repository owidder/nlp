import os
import argparse

from gensim import corpora, models

from python.words_of_file import create_words_dict, write_long_words_files_parallel
from python.tfidf import create_tfidf_files
from python.util.util import open_file_for_writing_with_path_creation
from python.aggregate import aggregate_folder_for_values, aggregate_folder_for_words
from python.git_info import create_base_url_files
from python.avgmax import avgmax


def termid_to_avgmax(termid: int, avgmax: list, id2word):
    term = id2word[termid]
    return len(avgmax) - avgmax.index(term)


def avgmax_for_doc(doc):
    return []

def create_corpus_avgmax(corpus_tfidf, id2word):
    [d[0] for d in corpus_tfidf]
    pass


def create_vectors(word_dict: dict, out_path: str, num_topics: int, vectors_file_name = "vectors2.csv", vectors_file_name_avgmax = "vectors_avgmax.csv"):
    vectors_out_path = f"{out_path}/{vectors_file_name}"
    vectors_out_path_avgmax = f"{out_path}/{vectors_file_name_avgmax}"

    if not (os.path.exists(vectors_out_path) and os.path.exists(vectors_out_path_avgmax)):
        print("---- create word dict ----")
        only_long_words = {file_path: list(filter(lambda w: len(w) > 2, list(map(lambda w2: w2.removesuffix("\n"), word_dict[file_path].split(' '))))) for file_path
                           in list(word_dict.keys())}
        documents = list(only_long_words.values())
        dictionary = corpora.Dictionary(documents)
        document_terms = [dictionary.doc2bow(doc) for doc in documents]

        print("--- create lsi model ----")
        tfidf = models.TfidfModel(document_terms)
        corpus_tfidf = tfidf[document_terms]
        word_ids = [list(map(lambda e: e[0], t)) for t in (list(d) for d in corpus_tfidf)]
        word_ids_with_avgmax = [[(w, termid_to_avgmax(w, avgmax, dictionary)) for w in word_ids[n]] for n in range(len(word_ids))]

        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
        lsi_avgmax = models.LsiModel(word_ids_with_avgmax, id2word=dictionary, num_topics=num_topics)

        vectors_out_file = open_file_for_writing_with_path_creation(vectors_out_path)
        vectors_out_file_avgmax = open_file_for_writing_with_path_creation(vectors_out_path_avgmax)

        print("---- create vectors ----")
        only_many_words = {file_path: only_long_words[file_path] for file_path in list(filter(lambda k: len(only_long_words[k]) > 1, only_long_words.keys()))}
        for i, file_rel_path in enumerate(only_many_words.keys()):
            vectors_out_list = [file_rel_path]
            vectors_out_list_avgmax = [file_rel_path]
            vec_bow = dictionary.doc2bow(only_many_words[file_rel_path])
            vec_lsi = lsi[vec_bow]
            vec_lsi_avgmax = lsi_avgmax[vec_bow]

            for entry in vec_lsi:
                vectors_out_list.append(str(round(entry[1], 2)))

            for entry_avgmax in vec_lsi_avgmax:
                vectors_out_list_avgmax.append(str(round(entry_avgmax[1], 2)))

            print("\t".join(vectors_out_list), file=vectors_out_file)
            print("\t".join(vectors_out_list_avgmax), file=vectors_out_file_avgmax)

            if i%100 == 0:
                print(i)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--docpath', required=True, action='store', help='Path to the documents')
    parser.add_argument('--outpath', required=True, action='store', help='Path to the output folder')
    args = parser.parse_args()

    write_long_words_files_parallel(doc_path=args.docpath, out_path=args.outpath)
    word_dict = create_words_dict(doc_path=args.docpath, out_path=args.outpath)
    create_tfidf_files(word_dict, out_path=args.outpath)
    create_vectors(word_dict, out_path=args.outpath, num_topics=2000)
    aggregate_folder_for_values(folder_path=f"{args.outpath}/tfidf")
    aggregate_folder_for_words(folder_path=f"{args.outpath}/words")
    create_base_url_files(doc_path=args.docpath, out_path=args.outpath)


if __name__ == "__main__":
    main()
