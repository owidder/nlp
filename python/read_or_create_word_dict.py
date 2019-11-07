from get_args import get_args
from words.words_of_file import read_or_create_word_dict
from words.term_filter_level import TermFilterLevel

if __name__ == '__main__':
    args = get_args(doc_path_required=True, dict_path_required=True, name_required=True, filterlevel_required=True, term_infos_name_required=True, term_infos_path_required=True)
    read_or_create_word_dict(doc_path=args.docpath, dict_path=args.dictpath, name=args.name, term_infos_name=args.term_infos_name, term_infos_path=args.term_infos_path, filter_level=TermFilterLevel[args.filterlevel])
