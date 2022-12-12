from flask import Blueprint

detail = Blueprint('detail', __name__, url_prefix='/detail')

from . import views
