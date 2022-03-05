import os
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim import corpora, models

from python.util.util import open_file_for_writing_with_path_creation


def create_tfidf_files(word_dict: dict, out_path: str) -> None:
    tfidf = TfidfVectorizer()
    doctermmatrix = tfidf.fit_transform(word_dict.values())
    feature_names_out = tfidf.get_feature_names_out()

    for doc_id in range(doctermmatrix.shape[0]):
        out_file_path = os.path.join(out_path, "tfidf", f"{list(word_dict.keys())[doc_id]}.tfidf.csv")
        out_file = open_file_for_writing_with_path_creation(out_file_path)
        for term_id in range(doctermmatrix.shape[1]):
            tfidf_value = doctermmatrix[doc_id, term_id]
            if tfidf_value > 0:
                print(f"{feature_names_out[term_id]}\t{str(round(tfidf_value, 2))}", file=out_file)

    corpus = [[(v, doctermmatrix[d, v]) for v in range(doctermmatrix.shape[1]) if doctermmatrix[d, v] > 0] for d in range(doctermmatrix.shape[0])]
    dictionary = {t: feature_names_out[t] for t in range(len(feature_names_out))}
    lsi = models.LsiModel(corpus=corpus, id2word=dictionary)

    vectors_out_file = open_file_for_writing_with_path_creation(f"{out_path}/vectors.csv")

    print("---- create vectors ----")
    for i, file_rel_path in enumerate(word_dict.keys()):
        vectors_out_list = [file_rel_path]
        content = word_dict[file_rel_path].split()
        vec_bow = [(list(feature_names_out).index(_), content.count(_)) for _ in set(content)]
        vec_lsi = lsi[vec_bow]

        for entry in vec_lsi:
            vectors_out_list.append(str(round(entry[1], 2)))

        print("\t".join(vectors_out_list), file=vectors_out_file)
