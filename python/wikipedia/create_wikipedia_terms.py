import re
import argparse

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


def create_wikipedia_terms(titles_path) -> Set[str]:
    terms = set()

    with open(titles_path) as titles_file:
        words = titles_file.readline()
        while words:
            words = remove_hex_chars(words)
            words = only_chars_and_numbers(words)
            words = remove_numbers(words)
            words = remove_single_chars(words)
            for word in words.split():
                print(word)
                terms.add(word)
            words = titles_file.readline()

    return terms


def write_terms(out_path: str, terms: Set[str]):
    terms_list = list(terms)
    terms_list.sort()
    with open(out_path, 'w') as out_file:
        for term in terms_list:
            out_file.write(f"{term}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--titles', required=True, action='store', help='Path to the wikipedia titles file')
    parser.add_argument('--out', required=True, action='store', help='Path to the output file')
    args = parser.parse_args()
    terms = create_wikipedia_terms(titles_path=args.titles)
    write_terms(out_path=args.out, terms=terms)
