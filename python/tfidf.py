import os
from sklearn.feature_extraction.text import TfidfVectorizer


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
