from nltk.tokenize import word_tokenize
from typing import Set

from python.stackexchange.tags import init_tags

terms: Set[str] = set()

def init_stackexchange_tags(tags_path='/Users/oliver/dev/github/nlpDocs/python/tech'):
    init_tags(terms, tags_path)


def is_tag(tag: str) -> bool:
    return (tag.lower() in terms) or (tag.lower() in terms)
