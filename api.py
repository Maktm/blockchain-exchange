"""API implementation for blockchain and wallet backend."""

from wallet import Wallet

from flask import Blueprint, jsonify, Response, request

from blockchain import Blockchain, Transaction

api = Blueprint('api', __name__, template_folder='templates')

blockchain = Blockchain()


@api.route('/api/wallet/create')
def new_wallet() -> Response:
    """Generates a new public/private keypair."""
    wallet = Wallet()
    return jsonify(wallet.get_json())


@api.route('/api/transaction/new', methods=['POST'])
def new_transaction() -> Response:
    """Add a new transaction to the blockchain."""
    values = request.form
    required = ('sender_address', 'sender_private_key', 'recipient_address', 'stock', 'quantity')

    for r in required:
        if r not in values:
            print(values)
            return Response('Missing form value', 400)

    transaction = Transaction(
        values['sender_address'],
        values['sender_private_key'],
        values['recipient_address'],
        values['stock'],
        values['quantity']
    )

    signature = transaction.sign()

    try:
        blockchain.submit_transaction(
            values['sender_address'],
            values['recipient_address'],
            values['stock'],
            values['quantity'],
            signature
        )
    except Exception as error:
        print("[!] Error: ", error)

    return Response('Successfully added', 200)


@api.route('/api/transaction/view')
def view_transaction() -> Response:
    """Returns a collection of all the added transactions."""
    return jsonify({
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    })
