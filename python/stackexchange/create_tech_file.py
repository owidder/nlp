from typing import Set

from .tags import init_tags


def create_tech_file(tags_path='/Users/oliver/dev/github/nlp/stackexchange'):
    terms: Set[str] = set()
    init_tags(terms, tags_path)
    tech_terms_file = open("./tech_terms.txt", "w")
    for term in terms:
        tech_terms_file.write(f"{term}\n")
    tech_terms_file.close()


if __name__ == "__main__":
    create_tech_file()
