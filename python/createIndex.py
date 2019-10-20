from gensim import corpora, models, similarities

from get_args import get_args

def create_index(dict_path, name):
    dictionary = corpora.Dictionary.load('./data/corpus.dict')
    corpus = corpora.MmCorpus('./data/corpus.mm')
    tfidf = models.TfidfModel(corpus)

    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)
    lsi.save('./data/corpus.lsi')
    corpus_lsi = lsi[corpus_tfidf]

    index = similarities.MatrixSimilarity(lsi[corpus])
    index.save('./data/corpus.100.index')


def main():
    args = get_args(dict_path_required=True, name_required=True)
    create_index(dict_path=args.dictpath, name=args.name)


if __name__ == "__main__":
    main()
