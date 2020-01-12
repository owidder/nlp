import os

from gensim import corpora, models, similarities

from words.words_of_file import read_or_create_word_dict, is_included, read_word_dict
from util.util import rel_path_from_abs_path
from get_args import get_args
from words.term_filter_level import TermFilterLevel
from util.dict_util import create_file_name


def create_matrix(doc_path, dict_path, name, term_infos_name='BASE', filter_level=TermFilterLevel.NONE, password=None):
    word_dict = read_word_dict(name, dict_path, term_infos_name, filter_level, password)
    documents = [word.split(' ') for word in list(word_dict.values())]
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=200)
    index = similarities.MatrixSimilarity(lsi[document_terms])

    matrix_out_file = open(f"{dict_path}/matrix-{name}.csv", 'w')
    vectors_out_file = open(f"{dict_path}/vectors-{name}.csv", 'w')
    whole_cloud_out_file = open(f"{dict_path}/whole_cloud-{name}.csv", 'w')

    for i, file_rel_path in enumerate(word_dict.keys()):
        matrix_out_list = [file_rel_path]
        vectors_out_list = [file_rel_path]
        content = word_dict[file_rel_path]
        vec_bow = dictionary.doc2bow(content.split())
        vec_lsi = lsi[vec_bow]
        sims = index[vec_lsi]
        ssims = sorted(enumerate(sims), key=lambda item: -item[1])

        for entry in vec_lsi:
            vectors_out_list.append(str(entry[1]))

        for tuple in list(enumerate(ssims))[:10]:
            rel_docname = list(word_dict.keys())[tuple[1][0]]
            str_value = str(tuple[1][1])
            if rel_docname != file_rel_path:
                matrix_out_list.append(rel_docname)
                matrix_out_list.append(str_value)

        tuple_list = []
        for tuple in list(enumerate(ssims)):
            j = tuple[1][0]
            # j>i: because of symmetry
            if j > i and tuple[1][1] > .5:
                tuple_list.append("%d\t%.4f" % (j, tuple[1][1]))

        print("\t".join(matrix_out_list), file=matrix_out_file)
        print("\t".join(vectors_out_list), file=vectors_out_file)
        print("\t".join(tuple_list), file=whole_cloud_out_file)

        i += 1
        if i%100 == 0:
            print(i)


def main():
    args = get_args(doc_path_required=True,
                    dict_path_required=True,
                    password_required=False,
                    name_required=True,
                    filterlevel_required=False,
                    term_infos_name_required=False)
    create_matrix(doc_path=args.docpath,
                  dict_path=args.dictpath,
                  name=args.name,
                  password=args.password,
                  filter_level=TermFilterLevel[args.filterlevel],
                  term_infos_name=args.term_infos_name)


if __name__ == "__main__":
    main()
