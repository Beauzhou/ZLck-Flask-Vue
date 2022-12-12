from flask import Blueprint

banner = Blueprint('banner', __name__, url_prefix='/banner')

from . import views
