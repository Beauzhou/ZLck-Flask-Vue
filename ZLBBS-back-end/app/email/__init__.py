from flask import Blueprint

email = Blueprint('email', __name__, url_prefix='/email')

from . import views
