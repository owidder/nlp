import os

from gensim import corpora, models, similarities

from get_args import get_args
from words.term_filter_level import TermFilterLevel
from util.dict_util import create_file_name
from words.words_of_file import read_word_dict


def create_index(dict_path, name, term_infos_name='BASE', filter_level=TermFilterLevel.NONE):
    word_dict = read_word_dict(name, dict_path, term_infos_name, filter_level)
    dictionary = corpora.Dictionary.load(os.path.join(dict_path, create_file_name('dictionary', name, term_infos_name, filter_level, 'dict')))
    doc_term_matrix = corpora.MmCorpus(os.path.join(dict_path, create_file_name('doc_term_matrix', name, term_infos_name, filter_level, 'mm')))
    tfidf = models.TfidfModel(doc_term_matrix)

    corpus_tfidf = tfidf[doc_term_matrix]
    documents = [word.split(' ') for word in list(word_dict.values())]

    for num_topics in range(3, 100):
        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
        coherence_model = models.coherencemodel.CoherenceModel(model=lsi, texts=documents, dictionary=dictionary, coherence='c_v')
        coherence_score = coherence_model.get_coherence()
        print(f"\nCoherence score for {num_topics} topics: {coherence_score}")


def main():
    args = get_args(dict_path_required=True, name_required=True, filterlevel_required=False, term_infos_name_required=False, term_infos_path_required=False)
    create_index(dict_path=args.dictpath, name=args.name)


if __name__ == "__main__":
    main()
