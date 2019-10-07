import re
import os
import errno

def rel_path_from_abs_path(base_path, abs_path):
    rel_path = re.sub(base_path, '', abs_path)
    if rel_path.startswith('/'):
        return rel_path[1:]
    else:
        return rel_path


def open_file_for_writing_with_path_creation(file_path, mode='w'):
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return open(file_path, mode)


