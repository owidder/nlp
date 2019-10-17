from collections import defaultdict

def remove_words_that_appear_only_once(texts):
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    return [[token for token in text if frequency[token] > 1] for text in texts]


