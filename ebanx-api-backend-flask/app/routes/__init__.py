from flask import Blueprint
routes = Blueprint('__routes__', __name__)

from .reset import *
from .event import *
from .balance import *
