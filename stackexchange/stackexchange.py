import csv
import re
import os

from nltk.tokenize import word_tokenize
from typing import Set


terms: Set[str] = set()


def init_stackexchange_tags(tags_path):
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
                            terms.add(row[1])
                            if row[1].find('-') > -1:
                                for part in row[1].split("-"):
                                    terms.add(part)


def is_tag(tag: str) -> bool:
    return (tag in terms)


def remove_non_stackexchange(words: str) -> str:
    tokens = word_tokenize(words)
    return " ".join(list(filter(lambda word: is_tag(word), tokens)))
