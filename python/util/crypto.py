import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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
    return base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
