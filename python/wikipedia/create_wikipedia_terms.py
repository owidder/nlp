import re
import argparse
import csv
import os

from typing import Set


def remove_hex_chars(words: str) -> str:
    return re.sub('%[0-9A-Fa-f][0-9A-Fa-f]', ' ', words)


def only_chars_and_numbers(words: str) -> str:
    return re.sub('[^0-9A-Za-z]+', ' ', words)


def remove_numbers(words: str) -> str:
    words = words.split()
    filtered_words = list(filter(lambda word: not word.isdigit(), words))
    return " ".join(filtered_words)


def remove_single_chars(words):
    return ' '.join([w for w in words.split() if len(w) > 1])


def create_wikipedia_terms(tags_path) -> Set[str]:
    terms: Set[str] = set()

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

    return terms


def write_terms(out_path: str, terms: Set[str]):
    terms_list = list(terms)
    terms_list.sort()
    with open(out_path, 'w') as out_file:
        for term in terms_list:
            out_file.write(f"{term}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tagspath', required=True, action='store', help='Path to the wikipedia tags files')
    parser.add_argument('--out', required=True, action='store', help='Path to the output file')
    args = parser.parse_args()
    terms = create_wikipedia_terms(tags_path=args.tagspath)
    write_terms(out_path=args.out, terms=terms)
