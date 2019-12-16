import mlflow

from gensim import corpora, models

from get_args import get_args
from words.term_filter_level import TermFilterLevel
from words.words_of_file import read_word_dict


def create_index(dict_path, name, term_infos_name='BASE', filter_level=TermFilterLevel.NONE):
    word_dict = read_word_dict(name, dict_path, term_infos_name, filter_level)
    documents = [word.split(' ') for word in list(word_dict.values())]
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    for num_topics in range(3, 5):
        with mlflow.start_run():
            mlflow.log_param("num_topics", num_topics)
            lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
            coherence_model = models.coherencemodel.CoherenceModel(model=lsi, texts=documents, dictionary=dictionary, coherence='c_v')
            coherence_score = coherence_model.get_coherence()
            mlflow.log_metric("coherence_score", coherence_score)
            print(f"\nCoherence score for {num_topics} topics: {coherence_score}")


def main():
    args = get_args(dict_path_required=True, name_required=True, filterlevel_required=False, term_infos_name_required=False, term_infos_path_required=False)
    create_index(dict_path=args.dictpath, name=args.name)


if __name__ == "__main__":
    main()
