import csv


term_dict = {}


def init_term_dict(name: str):
    with open(f"/Users/oliver/dev/github/nlpClient/server/termInfos.{name}.csv") as csv_file:
        for row in csv.reader(csv_file, delimiter=';'):
            term_dict[row[0]] = row[1]


def check_term_type(term: str, term_type: str) -> bool:
    return term in term_dict and term_dict[term] == term_type


def is_in_term(term: str) -> bool:
    return check_term_type(term, '+')


def is_out_term(term: str) -> bool:
    return check_term_type(term, '-')


def is_dontknow_term(term: str) -> bool:
    return check_term_type(term, '?')


def is_term_hard(term: str) -> bool:
    return is_in_term(term)


def is_term_soft(term: str) -> bool:
    return not is_out_term(term)


def is_term_medium(term: str) -> bool:
    return is_in_term(term) or is_dontknow_term(term)


