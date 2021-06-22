import functools
import mlflow
import os

from gensim import corpora, models
from typing import List

from get_args import get_args
from words.words_of_file import read_word_dict
from util.util import open_file_for_writing_with_path_creation


def write_topic(topic_num: int, topic: List[float], dictionary: corpora.Dictionary, outpath: str, num_topics: int, num_entries: int):
    topic_with_word = [{'word': dictionary[i], 'value': v} for i,v in enumerate(topic)]
    sorted_topic_with_word = sorted(topic_with_word, key=lambda e: abs(e['value']))
    reversed_sorted_topic_with_word = list(reversed(list(sorted_topic_with_word)))
    sub_sorted_topic_with_word = [reversed_sorted_topic_with_word[i] for i in list(range(num_entries))] if num_entries > 0 else reversed_sorted_topic_with_word
    topic_str = functools.reduce(lambda t, e: f"{t}{e['word']}\t{e['value']}\n", sub_sorted_topic_with_word, "")
    csvFile = open_file_for_writing_with_path_creation(f"{outpath}/_{str(num_topics).zfill(5)}/t{str(topic_num).zfill(5)}.csv")
    print(topic_str, file=csvFile)


def write_all_topics(lsi_model: models.LsiModel, dictionary: corpora.Dictionary, outpath: str, num_topics: int, num_entries: int):
    txtFile = open_file_for_writing_with_path_creation(f"{outpath}/_{str(num_topics).zfill(5)}/topics.txt")
    print(lsi_model.print_topics(), file=txtFile)
    for topic_num in range(0, len(lsi_model.get_topics())):
        write_topic(topic_num, lsi_model.get_topics()[topic_num], dictionary, outpath, num_topics, num_entries)


def create_index(dict_path, name, outpath=None, num_entries=0, min_topics=10, max_topics=50):
    word_dict_path = os.path.join(dict_path, f'word_dict.{name}')
    word_dict = read_word_dict(word_dict_path)
    documents = [word.split(' ') for word in list(word_dict.values())]
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    for num_topics in range(min_topics, max_topics+1):
        with mlflow.start_run():
            mlflow.log_param("num_topics", num_topics)
            lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
            if outpath is not None:
                write_all_topics(lsi, dictionary, outpath, num_topics, num_entries)
            coherence_model = models.coherencemodel.CoherenceModel(model=lsi, texts=documents, dictionary=dictionary, coherence='c_v')
            coherence_score = coherence_model.get_coherence()
            mlflow.log_metric("coherence_score", coherence_score)
            print(f"\nCoherence score for {num_topics} topics: {coherence_score}")


def main():
    args = get_args(dict_path_required=True,
                    name_required=True,
                    num_entries_required=True,
                    min_topics_required=True,
                    max_topics_required=True,
                    out_path_required=False)
    create_index(dict_path=args.dictpath,
                 name=args.name,
                 outpath=args.outpath,
                 num_entries=int(args.num_entries),
                 min_topics=int(args.min_topics), max_topics=int(args.max_topics))


if __name__ == "__main__":
    main()
