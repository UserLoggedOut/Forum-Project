from flask import Blueprint


user_blu = Blueprint("user", __name__)

from . import views

