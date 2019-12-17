from simplecrypt import encrypt

from get_args import get_args


def encrypt_file(filepath: str, password: str):
    file_to_encrypt = open(filepath, "r")
    encrypted_file = open(f"{filepath}.crypt", "w")
    unencrypted_content = file_to_encrypt.read()
    encrypted_content = encrypt(password, unencrypted_content)
    encrypted_file.write(encrypted_content)


if __name__ == '__main__':
    args = get_args(file_path_required=True, password_required=True)
    encrypt_file(args.filepath, args.password)
