import csv
import re
import os

from typing import Set

only_digits_regex = re.compile('^\d*$')
at_least_one_char_regex = re.compile('^.*[A-Za-z]+.*$')


def add_to_terms(word, terms):
    if at_least_one_char_regex.match(word):
        terms.add(word)


def init_tags(terms: Set[str], tags_path: str):
    file_pattern = re.compile("^.*\.tags\..*$")
    for subdir, dirs, files in os.walk(tags_path):
        for file in files:
            if file_pattern.match(file):
                tags_file_abs_path = os.path.join(subdir, file)
                print(tags_file_abs_path)
                with open(tags_file_abs_path) as tags_file:
                    csv_reader = csv.reader(tags_file, delimiter=",", quoting=csv.QUOTE_ALL)
                    for row in csv_reader:
                        if csv_reader.line_num > 1:
                            add_to_terms(row[1], terms)
                            if row[1].find('-') > -1:
                                for part in row[1].split("-"):
                                    add_to_terms(part, terms)
