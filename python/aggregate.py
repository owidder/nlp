import os
import argparse

VALUES_FILE_NAME = '_.csv'
TFIDF_SUFFIX = "tfidf.csv"
LONG_WORDS_SUFFIX = "_long_words_"
WORDS_FILE_NAME = "_._long_words_of_folder"

SUM_INDEX = 0
MAX_INDEX = 1
COUNT_INDEX = 2
WEIGHTED_SUM_INDEX = 3
WEIGHTED_MAX_INDEX = 4


def aggregate_words_in_file(file_path: str, current_words: set):
    with open(file_path, 'r') as f:
        for line in f:
            long_words = line.split(" ")
            current_words.update(long_words)


def aggregate_values_in_file(file_path: str, current_values: dict):
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split("\t")
            k = parts[0]
            if len(k) > 0:
                if file_path.endswith(VALUES_FILE_NAME):
                    sum_v = float(parts[1])
                    max_v = float(parts[2])
                    weighted_sum_v = float(parts[5])
                    weighted_max_v = float(parts[6])
                    count_v = float(parts[3])
                elif file_path.endswith(TFIDF_SUFFIX):
                    sum_v = float(parts[1])
                    max_v = float(parts[1])
                    weighted_sum_v = float(parts[2])
                    weighted_max_v = float(parts[2])
                    count_v = 1

                if k in current_values:
                    current_values[k][SUM_INDEX] += sum_v
                    current_values[k][MAX_INDEX] = max_v if current_values[k][MAX_INDEX] < max_v else current_values[k][MAX_INDEX]
                    current_values[k][COUNT_INDEX] += count_v
                    current_values[k][WEIGHTED_SUM_INDEX] += weighted_sum_v
                    current_values[k][WEIGHTED_MAX_INDEX] = weighted_max_v if current_values[k][WEIGHTED_MAX_INDEX] < weighted_max_v else current_values[k][WEIGHTED_MAX_INDEX]
                else:
                    current_values[k] = [None, None, None, None, None]
                    current_values[k][SUM_INDEX] = sum_v
                    current_values[k][MAX_INDEX] = max_v
                    current_values[k][COUNT_INDEX] = count_v
                    current_values[k][WEIGHTED_SUM_INDEX] = weighted_sum_v
                    current_values[k][WEIGHTED_MAX_INDEX] = weighted_max_v


def aggregate_words_in_subfolder(subdir_path: str, current_words: set):
    words_file = f"{subdir_path}/{WORDS_FILE_NAME}"
    if not os.path.isfile(words_file):
        aggregate_folder_for_words(subdir_path)

    aggregate_words_in_file(file_path=words_file, current_words=current_words)


def aggregate_values_in_subfolder(subdir_path: str, current_values: dict):
    print(f"dir: {subdir_path}")
    values_file = f"{subdir_path}/{VALUES_FILE_NAME}"
    if not os.path.isfile(values_file):
        aggregate_folder_for_values(subdir_path)

    aggregate_values_in_file(file_path=values_file, current_values=current_values)


def aggregate_folder_for_words(folder_path):
    current_words = set()

    for f in os.listdir(folder_path):
        full_path = f"{folder_path}/{f}"
        if(os.path.isfile(full_path)):
            if(f.endswith(LONG_WORDS_SUFFIX)):
                aggregate_words_in_file(file_path=full_path, current_words=current_words)
        else:
            aggregate_words_in_subfolder(subdir_path=full_path, current_words=current_words)

    with open(f"{folder_path}/{WORDS_FILE_NAME}", 'w') as out_file:
        print(" ".join(current_words), file=out_file)


def aggregate_folder_for_values(folder_path):
    values = {}

    for f in os.listdir(folder_path):
        full_path = f"{folder_path}/{f}"
        if(os.path.isfile(full_path)):
            if(f.endswith(TFIDF_SUFFIX)):
                aggregate_values_in_file(file_path=full_path, current_values=values)
        else:
            aggregate_values_in_subfolder(subdir_path=full_path, current_values=values)

    with open(f"{folder_path}/{VALUES_FILE_NAME}", 'w') as out_file:
        for k, v in values.items():
            count = v[COUNT_INDEX]
            sum = v[SUM_INDEX]
            max = v[MAX_INDEX]
            avg = sum / count
            weighted_sum = v[WEIGHTED_SUM_INDEX]
            weighted_max = v[WEIGHTED_MAX_INDEX]
            weighted_avg = weighted_sum / count
            line = f"{k}\t{str(round(sum, 2))}\t{str(round(max, 2))}\t{str(count)}\t{str(round(avg, 2))}" \
                   f"\t{str(round(weighted_sum, 2))}\t{str(round(weighted_max, 2))}\t{str(round(weighted_avg, 2))}"
            print(line, file=out_file)


def main():
    global VALUES_FILE_NAME
    global TFIDF_SUFFIX

    parser = argparse.ArgumentParser()
    parser.add_argument('--outpath', required=True, action='store', help='Path to the output folder')
    args = parser.parse_args()

    aggregate_folder_for_values(folder_path=f"{args.outpath}/tfidf")


if __name__ == "__main__":
    main()
