import os

from get_args import get_args


FOLDER_VALUES_FILE_NAME = '_.csv'


def aggregate_values_in_file(file_path, current_values):
    with open(file_path, 'r') as f:
        for line in f:
            kv = line.split("\t")
            k = kv[0]
            v = float(kv[1])
            if k in current_values:
                current_values[k] += v
            else:
                current_values[k] = v


def aggregate_values_in_subfolder(subdir_path, current_values):
    csv_values_file = f"{subdir_path}/{FOLDER_VALUES_FILE_NAME}"
    if not os.path.isfile(csv_values_file):
        aggregate_folder(subdir_path)

    aggregate_values_in_file(csv_values_file, current_values)


def aggregate_folder(folder_path):
    values = {}

    for f in os.listdir(folder_path):
        full_path = f"{folder_path}/{f}"
        if(os.path.isfile(full_path)):
            if(f.endswith('tfidf.csv')):
                aggregate_values_in_file(full_path, values)
        else:
            aggregate_values_in_subfolder(full_path, values)

    with open(f"{folder_path}/{FOLDER_VALUES_FILE_NAME}", 'w') as out_file:
        keys_sorted_after_values = sorted(values, key=values.__getitem__, reverse=True)
        for k in keys_sorted_after_values:
            print(f"{k}\t{str(values[k])}", file=out_file)


def main():
    args = get_args(out_path_required=True)
    aggregate_folder(folder_path=args.outpath)


if __name__ == "__main__":
    main()
