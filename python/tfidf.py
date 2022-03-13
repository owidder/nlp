import os
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim import models
import numpy

from python.util.util import open_file_for_writing_with_path_creation


def create_tfidf_files(business_terms_dict: dict, out_path: str) -> None:
    tfidf = TfidfVectorizer()
    doc_term_matrix = tfidf.fit_transform(business_terms_dict.values())
    feature_names_out = tfidf.get_feature_names_out()

    for doc_id in range(doc_term_matrix.shape[0]):
        file_name = f"{list(business_terms_dict.keys())[doc_id]}.tfidf.csv"
        print(f"create: {file_name}")
        out_file_path = os.path.join(out_path, "tfidf", file_name)
        if not os.path.exists(out_file_path):
            if not os.path.exists(os.path.dirname(out_file_path)):
                os.makedirs(os.path.dirname(out_file_path))
            out_file = open(out_file_path, mode="w")
            for term_id in range(doc_term_matrix.shape[1]):
                tfidf_value = doc_term_matrix[doc_id, term_id]
                if tfidf_value > 0:
                    print(f"{feature_names_out[term_id]}\t{str(round(tfidf_value, 2))}", file=out_file)

    print("---- create corpus ----")
    corpus = [[(v, doc_term_matrix[d, v]) for v in range(doc_term_matrix.shape[1]) if doc_term_matrix[d, v] > 0] for d in range(doc_term_matrix.shape[0])]
    print("---- create dictionary ----")
    dictionary = {t: feature_names_out[t] for t in range(len(feature_names_out))}
    print("---- create LsiModel ----")
    lsi = models.LsiModel(corpus=corpus, id2word=dictionary)

    vectors_out_file = open_file_for_writing_with_path_creation(f"{out_path}/vectors.csv")

    print("---- create vectors ----")
    for i, file_rel_path in enumerate(business_terms_dict.keys()):
        print(f"---> create vectors: {file_rel_path}")
        vectors_out_list = [file_rel_path]
        content = business_terms_dict[file_rel_path].split()
        print(content)
        vec_bow = [(list(feature_names_out).index(_), content.count(_)) for _ in set(content)]
        vec_lsi = lsi[vec_bow]

        for entry in vec_lsi:
            vectors_out_list.append(str(round(entry[1], 2)))

        print("\t".join(vectors_out_list), file=vectors_out_file)
