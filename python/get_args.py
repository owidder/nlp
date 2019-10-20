import argparse

def get_args(doc_path_required=False, dict_path_required=False, out_path_required=False, name_required=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--docpath', required=doc_path_required, action='store', help='Path to the documents')
    parser.add_argument('--dictpath', required=dict_path_required, action='store', help='Path to the dictionaries.')
    parser.add_argument('--outpath', required=out_path_required, action='store', help='Path to the output folder')
    parser.add_argument('--name', required=name_required, action='store', help='Name of the dictionary (see paramter --dictpath)')
    return parser.parse_args()