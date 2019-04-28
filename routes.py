"""Central storage location for the implementation of the URI routes."""

from flask import Flask, Response, render_template

from api import api

app = Flask(__name__)
app.register_blueprint(api)


@app.route('/')
def wallet() -> Response:
    """Index page."""
    return render_template('./wallet.html')


@app.route('/transaction/view')
def view_transaction() -> Response:
    """Returns a list of all the transactions added to the blockchain."""
    return render_template('./view_transaction.html')


@app.route('/transaction/new')
def new_transaction() -> Response:
    """Add a new transaction to the blockchain."""
    return render_template('./new_transaction.html')
