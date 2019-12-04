import os

from gensim import corpora, models, similarities

from words.words_of_file import read_or_create_word_dict, is_included
from util.util import rel_path_from_abs_path
from get_args import get_args
from words.term_filter_level import TermFilterLevel
from util.dict_util import create_file_name


def create_matrix(doc_path, dict_path, name, term_infos_path=None, term_infos_name='BASE', filter_level=TermFilterLevel.NONE):
    dictionary = corpora.Dictionary.load(os.path.join(dict_path, create_file_name('corpus', name, term_infos_name, filter_level, 'mm')))
    corpus = corpora.MmCorpus(f"{dict_path}/corpus-{name}-{term_infos_name}-{filter_level.value}.mm")

    lsi = models.LsiModel.load(os.path.join(dict_path, create_file_name('corpus', name, term_infos_name, filter_level, 'lsi')))
    index = similarities.MatrixSimilarity.load(os.path.join(dict_path, create_file_name('corpus_100', name, term_infos_name, filter_level, 'index')))

    # matrix_out_file = open(f"{dict_path}/matrix-{name}.csv", 'w')
    # vectors_out_file = open(f"{dict_path}/vectors-{name}.csv", 'w')

    word_unstem_dict = read_or_create_word_dict(doc_path=doc_path, dict_path=dict_path, name=name)

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
    args = get_args(doc_path_required=True, dict_path_required=True, name_required=True, filterlevel_required=False, term_infos_name_required=False, term_infos_path_required=False)
    create_matrix(doc_path=args.docpath, dict_path=args.dictpath, name=args.name)


if __name__ == "__main__":
    main()
