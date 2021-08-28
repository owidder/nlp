def add_words2_to_words1(words1: str, words2: str) -> str:
    if words1 is None:
        return words2
    elif words2 is None:
        return words1
    else:
        words1_list = words1.split(" ")
        words2_list = words2.split(" ")
        filtered_words2_list = list(filter(lambda word2: word2 not in words1_list, words2_list))
        return " ".join(words1_list + filtered_words2_list)


def merge_dict2_into_dict1(dict1, dict2):
    merge_2_into_1 = {file_rel_path: add_words2_to_words1(dict1.get(file_rel_path), words2) for file_rel_path, words2 in dict2.items()}
    return {file_rel_path: add_words2_to_words1(merge_2_into_1.get(file_rel_path), words1) for file_rel_path, words1 in dict1.items()}


def create_file_name(base: str, name: str):
    return f"{base}-{name}"
