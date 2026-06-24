"""
School Health Hub (SHH)
Encryption utility module implementing AES-256 equivalent symmetric encryption via Fernet.
Author: Ifende Daniel
"""

import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"


class DataEncyrpter:
    def __init__(self, key_file_path: str = KEY_FILE):
        self.key_file_path = key_file_path
        self._cipher_suite = Fernet(self._load_or_create_key())

    def _load_or_create_key(self) -> bytes:
        """
        Loads an existing cryptographic key or securely generates a new one
        if it does not exist locally.
        """
        if not os.path.exists(self.key_file_path):
            key = Fernet.generate_key()
            with open(self.key_file_path, "wb") as key_file:
                key_file.write(key)
        else:
            with open(self.key_file_path, "rb") as key_file:
                key = key_file.read()
        return key

    def encrypt(self, plain_text: str) -> str:
        """
        Encrypts a plaintext string and returns a safe UTF-8 string for database storage.
        """
        if not plain_text:
            return ""

        bytes_data = plain_text.encode("utf-8")
        encrypted_bytes = self._cipher_suite.encrypt(bytes_data)

        return encrypted_bytes.decode("utf-8")

    def decrypt(self, encrypted_text: str) -> str:
        """
        Decrypts an encrypted database string back to clear text.
        """
        if not encrypted_text:
            return ""

        try:
            bytes_data = encrypted_text.encode("utf-8")
            decrypted_bytes = self._cipher_suite.decrypt(bytes_data)
            return decrypted_bytes.decode("utf-8")
        except Exception as crypto_error:
            return f"[Decryption Error: {str(crypto_error)}]"
