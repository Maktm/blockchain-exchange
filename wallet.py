"""Wallet implementation."""

import binascii

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class Wallet:
    """
    A wallet is the core of a client that consists
    of the public/private keypair useable to process
    transactions for sending/receiving.
    """
    def __init__(self):
        """
        Generates a new wallet.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.private_key = private_key
        self.public_key = private_key.public_key()

    def get_private_key(self) -> bytes:
        """
        Returns the formatted private key DER as a string.
        """
        private_bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        return private_bytes

    def get_public_key(self) -> bytes:
        """
        Returns the formatted public key DER as a string.
        """
        public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return public_bytes

    def get_json(self):
        """
        Returns a JSON-formatted string containing the
        public/private keypair.
        """
        return {
            'private_key': binascii.hexlify(self.get_private_key()).decode('utf8'),
            'public_key': binascii.hexlify(self.get_public_key()).decode('utf8')
        }
