import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# from: https://nitratine.net/blog/post/encryption-and-decryption-in-python/
def generate_key(password_provided: str) -> str:
    password = password_provided.encode()
    salt = b'A3X9IGQu7zAJISmwCZYI2g8O527kgXRDQo21WDh6NsWwLHmnUct89MBDdjviuYq'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))


def get_content_of_encrypted_file(filepath: str, password: str) -> str:
    key = generate_key(password)
    decrypter = Fernet(key)
    file_to_decrypt = open(filepath, "r")
    encrypted_content = file_to_decrypt.read().encode()
    return decrypter.decrypt(encrypted_content).decode("utf-8")


def encrypt_string(string: str, password: str) -> str:
    key = generate_key(password)
    encrypter = Fernet(key)
    return encrypter.encrypt(string.encode()).decode("utf-8")


def decrypt_string(string: str, password: str) -> str:
    key = generate_key(password)
    decrypter = Fernet(key)
    return decrypter.decrypt(string.encode()).decode("utf-8")


def encrypt_bytes(b: bytes, password: str) -> bytes:
    key = generate_key(password)
    encrypter = Fernet(key)
    return encrypter.encrypt(b)


def decrypt_bytes(b: bytes, password: str) -> str:
    key = generate_key(password)
    decrypter = Fernet(key)
    return decrypter.decrypt(b)
