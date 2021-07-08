import os

from gensim import corpora, models

from words.words_of_file import create_word_and_tags_dict
from python.tfidf import find_features
from get_args import get_args, get_int_env_var, NUM_TOPICS


def create_vectors(word_dict, out_path, name, num_topis):
    print("---- create word dict ----")
    documents = [word.split(' ') for word in list(word_dict.values())]
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    print("--- create lsi model ----")
    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topis)

    vectors_out_file = open(f"{out_path}/vectors-{name}.csv", 'w')

    print("---- create vectors ----")
    for i, file_rel_path in enumerate(word_dict.keys()):
        vectors_out_list = [file_rel_path]
        content = word_dict[file_rel_path]
        vec_bow = dictionary.doc2bow(content.split())
        vec_lsi = lsi[vec_bow]

        for entry in vec_lsi:
            vectors_out_list.append(str(entry[1]))

        print("\t".join(vectors_out_list), file=vectors_out_file)

        if i%100 == 0:
            print(i)


def create_word_dict(doc_path):
    return create_word_and_tags_dict(doc_path=doc_path)[0]


def main():
    args = get_args(doc_path_required=True, out_path_required=True, name_required=True)
    word_dict = create_word_and_tags_dict(doc_path=args.docpath)[0]
    num_topics = get_int_env_var(NUM_TOPICS, 200)
    create_vectors(word_dict, out_path=args.outpath, name=f"{args.name}-{num_topics:04d}", num_topis=num_topics)
    find_features(word_dict, doc_path=args.docpath, out_path=os.path.join(args.outpath, f"tfidf-{num_topics:04d}"))


if __name__ == "__main__":
    main()