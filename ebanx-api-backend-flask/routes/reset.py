from . import routes
from flask import request
from ..utils import DB

@routes.route('/reset', methods=['POST'])
def reset():
    DB.reset()
    return '0', 200
