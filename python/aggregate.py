import os

from get_args import get_args, get_str_env_var, OUT_SUB_FOLDER


FOLDER_SUM_VALUES_FILE_NAME = '_sum.csv'
FOLDER_MAX_VALUES_FILE_NAME = '_max.csv'
FOLDER_AVG_VALUES_FILE_NAME = '_avg.csv'
FOLDER_COUNT_VALUES_FILE_NAME = '_count.csv'


def aggregate_values_in_file(sum_values_file_path: str, current_sum_values: dict,
                             max_values_file_path: str, current_max_values: dict,
                             count_values_file_path: str, current_count_values: dict):
    with open(sum_values_file_path, 'r') as sum_f:
        for sum_line in sum_f:
            sum_kv = sum_line.split("\t")
            sum_k = sum_kv[0]
            sum_v = float(sum_kv[1])
            if sum_k in current_sum_values:
                current_sum_values[sum_k] += sum_v
            else:
                current_sum_values[sum_k] = sum_v

    with open(count_values_file_path, 'r') as count_f:
        for count_line in count_f:
            count_k = count_line.split("\t")[0]
            if count_k in current_count_values:
                current_count_values[count_k] += 1
            else:
                current_count_values[count_k] = 1

    with open(max_values_file_path, 'r') as max_f:
        for max_line in max_f:
            max_kv = max_line.split("\t")
            max_k = max_kv[0]
            max_v = float(max_kv[1])
            if max_k in current_max_values:
                current_max_values[max_k] = max_v if current_max_values[max_k] < max_v else current_max_values[max_k]
            else:
                current_max_values[max_k] = max_v


def aggregate_values_in_subfolder(subdir_path: str, current_sum_values: dict, current_max_values: dict, current_count_values: dict):
    print(f"dir: {subdir_path}")
    csv_sum_values_file = f"{subdir_path}/{FOLDER_SUM_VALUES_FILE_NAME}"
    csv_max_values_file = f"{subdir_path}/{FOLDER_MAX_VALUES_FILE_NAME}"
    csv_count_values_file = f"{subdir_path}/{FOLDER_COUNT_VALUES_FILE_NAME}"
    if not os.path.isfile(csv_sum_values_file) or not os.path.isfile(csv_max_values_file):
        aggregate_folder(subdir_path)

    aggregate_values_in_file(sum_values_file_path=csv_sum_values_file, current_sum_values=current_sum_values,
                             max_values_file_path=csv_max_values_file, current_max_values=current_max_values,
                             count_values_file_path=csv_count_values_file, current_count_values=current_count_values)


def aggregate_folder(folder_path):
    sum_values = {}
    max_values = {}
    count_values = {}

    for f in os.listdir(folder_path):
        full_path = f"{folder_path}/{f}"
        if(os.path.isfile(full_path)):
            if(f.endswith('tfidf.csv')):
                aggregate_values_in_file(sum_values_file_path=full_path, current_sum_values=sum_values,
                                         max_values_file_path=full_path, current_max_values=max_values,
                                         count_values_file_path=full_path, current_count_values=count_values)
        else:
            aggregate_values_in_subfolder(subdir_path=full_path, current_sum_values=sum_values, current_max_values=max_values, current_count_values=count_values)

    with open(f"{folder_path}/{FOLDER_SUM_VALUES_FILE_NAME}", 'w') as out_file:
        sum_keys_sorted_after_values = sorted(sum_values, key=sum_values.__getitem__, reverse=True)
        for k in sum_keys_sorted_after_values:
            print(f"{k}\t{str(sum_values[k])}", file=out_file)

    with open(f"{folder_path}/{FOLDER_MAX_VALUES_FILE_NAME}", 'w') as out_file:
        max_keys_sorted_after_values = sorted(max_values, key=max_values.__getitem__, reverse=True)
        for k in max_keys_sorted_after_values:
            print(f"{k}\t{str(max_values[k])}", file=out_file)

    with open(f"{folder_path}/{FOLDER_COUNT_VALUES_FILE_NAME}", 'w') as out_file:
        count_keys_sorted_after_values = sorted(count_values, key=count_values.__getitem__, reverse=True)
        for k in count_keys_sorted_after_values:
            print(f"{k}\t{str(count_values[k])}", file=out_file)

    with open(f"{folder_path}/{FOLDER_AVG_VALUES_FILE_NAME}", 'w') as out_file:
        count_keys_sorted_after_values = sorted(count_values, key=count_values.__getitem__, reverse=True)
        for k in count_keys_sorted_after_values:
            print(f"{k}\t{str(round(sum_values[k] /  count_values[k], 2))}", file=out_file)


def main():
    args = get_args(out_path_required=True)
    out_sub_folder = get_str_env_var(OUT_SUB_FOLDER, "")
    out_path = os.path.join(args.outpath, out_sub_folder)
    aggregate_folder(folder_path=out_path)


if __name__ == "__main__":
    main()
