from util.get_args import get_args
from words.words_of_file import read_or_create_word_unstem_dict

if __name__ == '__main__':
    args = get_args(doc_path_required=True, dict_path_required=True, name_required=True)
    word_unstem_dicts = read_or_create_word_unstem_dict(doc_path=args.docpath, dict_path=args.dictpath, name=args.name)


