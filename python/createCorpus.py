from gensim import corpora

from util.get_args import get_args
from util.word_utils import remove_words_that_appear_only_once
from words.words_of_file import read_or_create_word_unstem_dict


def create_corpus(doc_path, word_dict_path, name, out_path):
    word_unstem_dict = read_or_create_word_unstem_dict(doc_path=doc_path, dict_path=word_dict_path, name=name)
    texts = [[word for word in document.lower().split()] for document in list(word_unstem_dict.word_dict.values())]
    dictionary = corpora.Dictionary(remove_words_that_appear_only_once(texts))
    dictionary.save(f"{out_path}/corpus-{name}.dict")
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(f"{out_path}/corpus-{name}.mm", corpus)


def main():
    args = get_args(doc_path_required=True, dict_path_required=True, out_path_required=True, name_required=True)
    create_corpus(doc_path=args.docpath, word_dict_path=args.dictpath, out_path=args.outpath, name=args.name)


if __name__ == "__main__":
    main()
