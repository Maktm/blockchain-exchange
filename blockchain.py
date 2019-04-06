"""
Blockchain.
"""

from flask import Flask

app = Flask(__name__)

class Blockchain:
    # A representation of a blockchain that is
    # capable of transferring and mining data.
    pass

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    # Processes a new transaction in which data
    # is transferred from one wallet to another.
    return "TODO: New transaction"

@app.route('/transactions/get', methods=['GET'])
def get_transactions():
    # Returns a collection of the transactions
    # stored inside of the blockchain.
    return "TODO: Get transactions"

@app.route('/transactions/filter', methods=['GET'])
def filter_transactions():
    # Returns a filtered version of get_transactions
    # using the parameters provided by the user.
    return "TODO: Filter transactions"