from flask import Blueprint


user_blu = Blueprint("user_blu", __name__)

from . import views

