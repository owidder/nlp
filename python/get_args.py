import argparse


def get_args(
        doc_path_required=False,
        dict_path_required=False,
        out_path_required=False,
        name_required=False,
        filterlevel_required=False,
        term_infos_name_required=False,
        term_infos_path_required=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--docpath', required=doc_path_required, action='store', help='Path to the documents')
    parser.add_argument('--dictpath', required=dict_path_required, action='store', help='Path to the dictionaries.')
    parser.add_argument('--outpath', required=out_path_required, action='store', help='Path to the output folder')
    parser.add_argument('--name', required=name_required, action='store', help='Name of the dictionary (see paramter --dictpath)')
    parser.add_argument('--filterlevel', required=filterlevel_required, action='store', help='NONE / SOFT / MEDIUM / HARD')
    parser.add_argument('--term_infos_name', required=term_infos_name_required, action='store', help='termInfo.<term_infos_name>.csv')
    parser.add_argument('--term_infos_path', required=term_infos_path_required, action='store', help='path to termInfo.<term_infos_name>.csv')
    return parser.parse_args()
