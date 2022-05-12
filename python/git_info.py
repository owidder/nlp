import os
from git import Repo
from python.util.util import open_file_for_writing_with_path_creation

def is_repository_root(path: str):
    return os.path.isdir(os.path.join(path, ".git"))


def get_base_url(path_to_repo: str):
    repo = Repo(path_to_repo)
    commit_sha: str = repo.head.commit.hexsha
    remote_url: str = repo.remotes.origin.url

    base_url = "???"
    if remote_url.startswith("https://github.com"):
        base_url = f"{remote_url[0:-4]}/tree/{commit_sha}"
    elif remote_url.startswith("git@github.com:"):
        base_url = f"https://github.com/{remote_url[len('git@github.com:'):-4]}/tree/{commit_sha}"

    return base_url


def create_base_url_files(doc_path: str, out_path: str):
    for folder in os.listdir(doc_path):
        path_to_repo = os.path.join(doc_path, folder)
        if is_repository_root(path_to_repo):
            base_url = get_base_url(path_to_repo)
            base_url_file = open_file_for_writing_with_path_creation(f"{os.path.join(out_path)}/info/{folder}/base_url.txt")
            print(base_url, file=base_url_file)


if __name__ == "__main__":
    create_base_url_files("/Users/oliverwidder/dev/erp_doc", "/Users/oliverwidder/dev/github/nlp/dict/_all/antlr")
