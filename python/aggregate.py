import os
import argparse

VALUES_FILE_NAME = '_.csv'
SUFFIX = "tfidf.csv"

SUM_INDEX = 0
MAX_INDEX = 1
COUNT_INDEX = 2
WEIGHTED_SUM_INDEX = 3
WEIGHTED_MAX_INDEX = 4


def aggregate_values_in_file(file_path: str, current_values):
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split("\t")
            k = parts[0]
            if len(k) > 0:
                if file_path.endswith("_.csv"):
                    sum_v = float(parts[1])
                    max_v = float(parts[2])
                    weighted_sum_v = float(parts[5])
                    weighted_max_v = float(parts[6])
                    count_v = float(parts[3])
                else:
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


def aggregate_values_in_subfolder(subdir_path: str, current_values: dict):
    print(f"dir: {subdir_path}")
    values_file = f"{subdir_path}/{VALUES_FILE_NAME}"
    if not os.path.isfile(values_file):
        aggregate_folder(subdir_path)

    aggregate_values_in_file(file_path=values_file, current_values=current_values)


def aggregate_folder(folder_path):
    values = {}

    for f in os.listdir(folder_path):
        full_path = f"{folder_path}/{f}"
        if(os.path.isfile(full_path)):
            if(f.endswith(SUFFIX)):
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
    global SUFFIX

    parser = argparse.ArgumentParser()
    parser.add_argument('--outpath', required=True, action='store', help='Path to the output folder')
    args = parser.parse_args()

    aggregate_folder(folder_path=f"{args.outpath}/tfidf")


if __name__ == "__main__":
    main()
