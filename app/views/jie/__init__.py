from flask import Blueprint


jie_blu = Blueprint("jie_blu", __name__)

from . import views
