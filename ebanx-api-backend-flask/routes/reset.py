from . import routes
from flask import request

@routes.route('/reset', methods=['POST'])
def reset():
    return 'Reset'
