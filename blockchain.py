"""Blockchain implementation."""

import json

import hashlib

import binascii

from time import time

from random import randrange

from collections import OrderedDict

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Transaction:
    """
    Represents a single transaction between two wallets.
    """
    def __init__(self, sender_address, sender_private_key, recipient_address, stock, quantity) -> None:
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.stock = stock
        self.quantity = quantity

    def to_dict(self) -> OrderedDict:
        return OrderedDict({
            'sender_address': self.sender_address,
            'recipient_address': self.recipient_address,
            'stock': self.stock,
            'quantity': self.quantity
        })

    def sign(self):
        """
        Sign the transaction using a private key.
        """
        private_key = serialization.load_pem_private_key(
            binascii.unhexlify(self.sender_private_key.encode('utf8')),
            password=None,
            backend=default_backend()
        )
        signature = private_key.sign(
            str(self.to_dict()).encode('utf8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return signature


class Blockchain:
    """Blockchain."""
    def __init__(self):
        self.transactions = []
        self.chain = []

        # Genesis block
        self.create_block(0, '00')

    def submit_transaction(self, sender_address, recipient_address, stock, quanitity, signature):
        """
        Verify signature and add the transaction if True.
        """
        print("self.transactions=", len(self.transactions))

        transaction = OrderedDict({
            'sender_address': sender_address,
            'recipient_address': recipient_address,
            'stock': stock,
            'quantity': quanitity
        })

        verified = self.verify_signature(sender_address, signature, transaction)
        if verified:
            self.transactions.append(transaction)
            print('Added tranasaction successfully (len={})'.format(len(self.transactions)))
            self.mine()
            return len(self.chain) + 1
        else:
            raise Exception("Failed to add transaction to blockchain")

    def verify_signature(self, sender_address: str, signature, transaction: dict) -> bool:
        """
        Verify that the transaction is not faulty or fraudulent.
        """
        try:
            public_key = serialization.load_pem_public_key(
                binascii.unhexlify(sender_address.encode('utf8')),
                backend=default_backend()
            )
            public_key.verify(
                signature,
                str(transaction).encode('utf8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        except:
            return False
        return True

    def hash(self, block):
        """Create hash for blocks."""
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def mine(self):
        """Mine new block for transactions collected."""
        last_block = self.chain[-1]

        nonce = self.proof_of_work()
        previous_hash = self.hash(last_block)
        self.create_block(nonce, previous_hash)

    def proof_of_work(self) -> int:
        """Lazy PoW algorithm."""
        return randrange(0, 1000)

    def create_block(self, nonce, previous_hash) -> None:
        """Create a new block to be added to the chain."""
        block = {
            'block_number': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'nonce': nonce,
            'previous_hash': previous_hash
        }

        self.transactions = []
        self.chain.append(block)
