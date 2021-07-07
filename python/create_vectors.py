from gensim import corpora, models

from words.words_of_file import create_word_and_tags_dict
from get_args import get_args


def create_vectors(doc_path, out_path, name):
    print("---- create word dict ----")
    _word_dict = create_word_and_tags_dict(doc_path=doc_path, with_stemming=False)
    word_dict = _word_dict[0]
    documents = [word.split(' ') for word in list(word_dict.values())]
    dictionary = corpora.Dictionary(documents)
    document_terms = [dictionary.doc2bow(doc) for doc in documents]

    print("--- create lsi model ----")
    tfidf = models.TfidfModel(document_terms)
    corpus_tfidf = tfidf[document_terms]

    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=200)

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


def main():
    args = get_args(doc_path_required=True, out_path_required=True, name_required=True)
    create_vectors(doc_path=args.docpath, out_path=args.outpath, name=args.name)


if __name__ == "__main__":
    main()
