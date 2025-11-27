from cryptography.fernet import Fernet
import os

class SecurityUtils:
    def __init__(self):
        self.key = os.environ.get('SECURITY_KEY').encode()
        self.cipher = Fernet(self.key)

    def encrypt(self, data: str) -> str:
        """Encrypts the given data."""
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, token: str) -> str:
        """Decrypts the given token."""
        return self.cipher.decrypt(token.encode()).decode()

    def generate_key(self) -> str:
        """Generates a new encryption key."""
        return Fernet.generate_key().decode()