from gensim import corpora

from get_args import get_args
from util.word_utils import remove_words_that_appear_only_once
from words.words_of_file import read_or_create_word_dict
from words.term_filter_level import TermFilterLevel


def create_corpus(doc_path, dict_path, name, filter_level: TermFilterLevel):
    word_dict = read_or_create_word_dict(doc_path=doc_path, dict_path=dict_path, name=name, filter_level=filter_level)
    texts = [[word for word in document.lower().split()] for document in list(word_dict.values())]
    dictionary = corpora.Dictionary(remove_words_that_appear_only_once(texts))
    dictionary.save(f"{dict_path}/dictionary-{name}.dict")
    doc_term_matrix = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(f"{dict_path}/doc_term_matrix-{name}.mm", doc_term_matrix)


def main():
    args = get_args(doc_path_required=True, dict_path_required=True, name_required=True, filterlevel_required=True)
    create_corpus(doc_path=args.docpath, dict_path=args.dictpath, name=args.name, filter_level=TermFilterLevel[args.filterlevel])


if __name__ == "__main__":
    main()
