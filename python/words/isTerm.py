import csv
import os


term_infos = {}


def init_term_infos(term_infos_path: str, name: str):
    if term_infos_path is not None:
        with open(os.path.join(term_infos_path, f"termInfos.{name}.csv")) as csv_file:
            for row in csv.reader(csv_file, delimiter=';'):
                term_infos[row[0]] = row[1]


def check_term_type(term: str, term_type: str) -> bool:
    termLc = term.lower()
    return termLc in term_infos and term_infos[termLc] == term_type


def is_in_term(term: str) -> bool:
    return check_term_type(term, '+')


def is_out_term(term: str) -> bool:
    return check_term_type(term, '-')


def is_dontknow_term(term: str) -> bool:
    return check_term_type(term, '?')


def is_term_hard(term: str) -> bool:
    is_term = is_in_term(term)
    print(f"isterm\t{term}\t{is_term}")
    return is_term


def is_term_soft(term: str) -> bool:
    is_term = not is_out_term(term)
    print(f"isterm\t{term}\t{is_term}")
    return is_term


def is_term_medium(term: str) -> bool:
    is_term = is_in_term(term) or is_dontknow_term(term)
    print(f"isterm\t{term}\t{is_term}")
    return is_term
