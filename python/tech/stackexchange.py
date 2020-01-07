from nltk.tokenize import word_tokenize
from typing import Set

from tech.tags import *


terms: Set[str] = set()


def init_stackexchange_tags(tags_path='/Users/oliver/dev/github/nlpDocs/python/tech'):
    init_tags(terms, tags_path)


def is_tag(tag: str) -> bool:
    return (tag.lower() in terms) or (tag.lower() in terms)


def remove_non_stackexchange(words: str) -> str:
    tokens = word_tokenize(words)
    return " ".join(list(filter(lambda word: is_tag(word), tokens)))
