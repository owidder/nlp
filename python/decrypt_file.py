from cryptography.fernet import Fernet

from get_args import get_args
from util.crypto import generate_key


def decrypt_file(filepath: str, password: str):
    key = generate_key(password)
    decrypter = Fernet(key)
    file_to_decrypt = open(filepath, "r")
    encrypted_content = file_to_decrypt.read().encode()
    print(decrypter.decrypt(encrypted_content).decode("utf-8"))


if __name__ == '__main__':
    args = get_args(file_path_required=True, password_required=True)
    decrypt_file(args.filepath, args.password)
