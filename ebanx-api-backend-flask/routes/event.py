from flask import request, make_response, Response

from . import routes
from ..utils import DB
from ..utils.exceptions import NonExistingAccountException

@routes.route('/event', methods=['POST'])
def event():
    try:
        response_json = DB.event(**request.form)
        return response_json, 201

    except NonExistingAccountException:
        return '0', 404
