from flask import request
from . import routes

@routes.route('/balance', methods=['GET'])
def balance():
    account_id = request.args.get('account_id')

    if account_id is None:
        return ('0', 404)

    return f'Balance {account_id}'
