from flask import Blueprint


tiwen_blu = Blueprint("tiwen_blu", __name__)

from . import views
