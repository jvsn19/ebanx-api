from . import routes
from flask import request
from ..db import CustomDatabase

@routes.route('/reset', methods=['POST'])
def reset():
    CustomDatabase.reset()
    return '0', 200
