import os

from gensim import corpora, models, similarities

from words.words_of_file import read_or_create_word_unstem_dict, is_included
from util.util import rel_path_from_abs_path
from get_args import get_args

def create_matrix(doc_path, dict_path, name):
    dictionary = corpora.Dictionary.load(f"{dict_path}/corpus-{name}.dict")
    corpus = corpora.MmCorpus(f"{dict_path}/corpus-{name}.mm")

    lsi = models.LsiModel.load(f"{dict_path}/corpus-{name}.lsi")
    index = similarities.MatrixSimilarity.load(f"{dict_path}/corpus_100-{name}.index")

    # matrix_out_file = open(f"{dict_path}/matrix-{name}.csv", 'w')
    # vectors_out_file = open(f"{dict_path}/vectors-{name}.csv", 'w')

    word_unstem_dict = read_or_create_word_unstem_dict(doc_path=doc_path, dict_path=dict_path, name=name)

    for subdir, dirs, files in os.walk(doc_path):
        for file in files:
            file_abs_path = os.path.join(subdir, file)
            if is_included(file_abs_path):
                matrix_out_list = [file_abs_path]
                vectors_out_list = [file_abs_path]
                file_rel_path = rel_path_from_abs_path(base_path=doc_path, abs_path=file_abs_path)
                content = word_unstem_dict.word_dict[file_rel_path]
                vec_bow = dictionary.doc2bow(content.lower().split())
                vec_lsi = lsi[vec_bow]
                sims = index[vec_lsi]
                ssims = sorted(enumerate(sims), key=lambda item: -item[1])
                for entry in vec_lsi:
                    vectors_out_list.append(str(entry[1]))
                print(ssims)

                # for tuple in list(enumerate(ssims))[:10]:
                #     rel_docname = docnames[tuple[1][0]]
                #     str_value = str(tuple[1][1])
                #     if rel_docname != docname:
                #         matrix_out_list.append(rel_docname)
                #         matrix_out_list.append(str_value)
                #
                # print("\t".join(matrix_out_list), file=matrix_out_file)
                # print("\t".join(vectors_out_list), file=vectors_out_file)


def main():
    args = get_args(doc_path_required=True, dict_path_required=True, name_required=True)
    create_matrix(doc_path=args.docpath, dict_path=args.dictpath, name=args.name)


if __name__ == "__main__":
    main()
