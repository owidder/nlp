import os
import argparse

VALUES_FILE_NAME = '_.csv'
SUFFIX = "tfidf.csv"

SUM_INDEX = 0
MAX_INDEX = 1
COUNT_INDEX = 2


def aggregate_values_in_file(file_path: str, current_values):
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split("\t")
            k = parts[0]
            if len(k) > 0:
                if len(parts) > 2:
                    sum_v = float(parts[SUM_INDEX+1])
                    max_v = float(parts[MAX_INDEX+1])
                    count_v = int(parts[COUNT_INDEX+1])
                else:
                    sum_v = float(parts[1])
                    max_v = float(parts[1])
                    count_v = 1

                if k in current_values:
                    current_values[k][SUM_INDEX] += sum_v
                    current_values[k][COUNT_INDEX] += count_v
                    current_values[k][MAX_INDEX] = max_v if current_values[k][MAX_INDEX] < max_v else current_values[k][MAX_INDEX]
                else:
                    current_values[k] = [None, None, None]
                    current_values[k][SUM_INDEX] = sum_v
                    current_values[k][COUNT_INDEX] = count_v
                    current_values[k][MAX_INDEX] = max_v


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
            line = f"{k}\t{str(round(v[SUM_INDEX], 2))}\t{str(round(v[MAX_INDEX], 2))}\t{str(v[COUNT_INDEX])}\t{str(round(v[SUM_INDEX]/v[COUNT_INDEX], 2))}"
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
