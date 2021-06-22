import os

from gensim import corpora, models, similarities

from get_args import get_args
from words.words_of_file import read_word_dict


def create_index(dict_path, name):
    word_dict_path = os.path.join(dict_path, f'word_dict.{name}')
    word_dict = read_word_dict(word_dict_path)
    dictionary = corpora.Dictionary.load(os.path.join(dict_path, f'dictionary-{name}.dict'))
    doc_term_matrix = corpora.MmCorpus(os.path.join(dict_path, f'doc_term_matrix-{name}.mm'))
    tfidf = models.TfidfModel(doc_term_matrix)

    corpus_tfidf = tfidf[doc_term_matrix]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)
    lsi.save(f"{dict_path}/corpus-{name}.lsi")

    index = similarities.MatrixSimilarity(lsi[doc_term_matrix])
    index.save(f"{dict_path}/corpus_100-{name}.index")

    documents = [word.split(' ') for word in list(word_dict.values())]
    coherence_model = models.coherencemodel.CoherenceModel(model=lsi, texts=documents, dictionary=dictionary, coherence='c_v')
    coherence_score = coherence_model.get_coherence()
    print(coherence_score)


def main():
    args = get_args(dict_path_required=True,
                    name_required=True)
    create_index(dict_path=args.dictpath, name=args.name)


if __name__ == "__main__":
    main()
