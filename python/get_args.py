import argparse
import distutils.util
import os


def get_args(
        doc_path_required=False,
        dict_path_required=False,
        out_path_required=False,
        name_required=False,
        filterlevel_required=False,
        term_infos_name_required=False,
        term_infos_path_required=False,
        file_path_required=False,
        password_required=False,
        min_topics_required=False,
        max_topics_required=False,
        with_tags_required=False,
        num_entries_required=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--docpath', required=doc_path_required, action='store', help='Path to the documents')
    parser.add_argument('--dictpath', required=dict_path_required, action='store', help='Path to the dictionaries.')
    parser.add_argument('--outpath', required=out_path_required, action='store', help='Path to the output folder')
    parser.add_argument('--name', required=name_required, action='store', help='Name of the dictionary (see paramter --dictpath)')
    parser.add_argument('--filterlevel', required=filterlevel_required, action='store', help='NONE / SOFT / MEDIUM / HARD')
    parser.add_argument('--term_infos_name', required=term_infos_name_required, action='store', help='termInfo.<term_infos_name>.csv')
    parser.add_argument('--term_infos_path', required=term_infos_path_required, action='store', help='path to termInfo.<term_infos_name>.csv')
    parser.add_argument('--filepath', required=file_path_required, action='store', help='path to file (e.g. to encrypt)')
    parser.add_argument('--password', required=password_required, action='store', help='password to encrypt file')
    parser.add_argument('--num_entries', required=num_entries_required, action='store', help='number of entries')
    parser.add_argument('--min_topics', required=min_topics_required, action='store', help='min number of topics')
    parser.add_argument('--max_topics', required=max_topics_required, action='store', help='max number of topics')
    parser.add_argument('--with_tags', required=with_tags_required, action='store', help='use stackexchange tags')
    return parser.parse_args()


def get_bool_env_var(name: str, defvalue: bool) -> bool:
    if name in list(os.environ.keys()):
        return bool(distutils.util.strtobool(os.environ[name]))
    else:
        return defvalue


def get_int_env_var(name: str, defvalue: int) -> int:
    if name in list(os.environ.keys()):
        return int(os.environ[name])
    else:
        return defvalue

def get_str_env_var(name: str, defvalue: str) -> str:
    if name in list(os.environ.keys()):
        return os.environ[name]
    else:
        return defvalue


def get_float_env_var(name: str, defvalue: float) -> float:
    if name in list(os.environ.keys()):
        return float(os.environ[name])
    else:
        return defvalue


NUM_TOPICS = "NUM_TOPICS"
OUT_SUB_FOLDER = "OUT_SUB_FOLDER"
INCLUDE_FOLDERS = "INCLUDE_FOLDERS"
EXCLUDE_FOLDERS = "EXCLUDE_FOLDERS"

