import re
import argparse


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


def create_wikipedia_terms(titles_path, out_path):
    open(out_path, 'w').close()
    with open(out_path, 'a') as out_file:
        with open(titles_path) as titles_file:
            words = titles_file.readline()
            while words:
                words = remove_hex_chars(words)
                words = only_chars_and_numbers(words)
                words = remove_numbers(words)
                words = remove_single_chars(words)
                for word in words.split():
                    out_file.write(f"{word}\n")
                words = titles_file.readline()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--titles', required=True, action='store', help='Path to the wikipedia titles file')
    parser.add_argument('--out', required=True, action='store', help='Path to the output file')
    args = parser.parse_args()
    create_wikipedia_terms(titles_path=args.titles, out_path=args.out)
