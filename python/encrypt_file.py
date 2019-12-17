from cryptography.fernet import Fernet

from get_args import get_args
from util.crypto import generate_key


def encrypt_file(filepath: str, password: str):
    key = generate_key(password)
    encrypter = Fernet(key)
    file_to_encrypt = open(filepath, "r")
    encrypted_file = open(f"{filepath}.crypt", "w")
    unencrypted_content = file_to_encrypt.read().encode()
    encrypted_content = encrypter.encrypt(unencrypted_content)
    encrypted_file.write(encrypted_content)


if __name__ == '__main__':
    args = get_args(file_path_required=True, password_required=True)
    encrypt_file(args.filepath, args.password)
