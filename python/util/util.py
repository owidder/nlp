import re

def rel_path_from_abs_path(base_path, abs_path):
    rel_path = re.sub(base_path, '', abs_path)
    if rel_path.startswith('/'):
        return rel_path[1:]
    else:
        return rel_path

