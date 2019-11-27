from nltk.tokenize import word_tokenize
from typing import Set

from .tags import init_tags


terms: Set[str] = set()


def init_stackexchange_tags(tags_path='/Users/oliver/dev/github/nlp/stackexchange'):
    init_tags(terms, tags_path)


def is_tag(tag: str) -> bool:
    return (tag.lower() in terms) or (tag.lower() in terms)


def remove_non_stackexchange(words: str) -> str:
    tokens = word_tokenize(words)
    return " ".join(list(filter(lambda word: is_tag(word), tokens)))
