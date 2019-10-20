from gensim import corpora, models, similarities

from get_args import get_args

def create_index(dict_path, name):
    dictionary = corpora.Dictionary.load(f"{dict_path}/corpus-{name}.dict")
    corpus = corpora.MmCorpus(f"{dict_path}/corpus-{name}.mm")
    tfidf = models.TfidfModel(corpus)

    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)
    lsi.save(f"{dict_path}/corpus-{name}.lsi")

    index = similarities.MatrixSimilarity(lsi[corpus])
    index.save(f"{dict_path}/corpus_100-{name}.index")


def main():
    args = get_args(dict_path_required=True, name_required=True)
    create_index(dict_path=args.dictpath, name=args.name)


if __name__ == "__main__":
    main()
