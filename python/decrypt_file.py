from get_args import get_args
from util.crypto import get_content_of_encrypted_file


def decrypt_file(filepath: str, password: str):
    print(get_content_of_encrypted_file(filepath, password))


if __name__ == '__main__':
    args = get_args(file_path_required=True, password_required=True)
    decrypt_file(args.filepath, args.password)
