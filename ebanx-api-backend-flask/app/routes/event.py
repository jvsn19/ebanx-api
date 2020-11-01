from flask import request, make_response, Response

from . import routes
from ..utils.exceptions import NonExistingAccountException
from ..db import CustomDatabase

@routes.route('/event', methods=['POST'])
def event():
    try:
        response_json = CustomDatabase.event(**request.form)
        return response_json, 201

    except NonExistingAccountException:
        return '0', 404
