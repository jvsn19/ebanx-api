from flask import request
from . import routes

from ..utils.exceptions import NonExistingAccountException

from ..utils import DB

@routes.route('/balance', methods=['GET'])
def balance():
    account_id = request.args.get('account_id')
    try:
        return str(DB.balance(account_id)), 200
    except NonExistingAccountException:
        return '0', 404
