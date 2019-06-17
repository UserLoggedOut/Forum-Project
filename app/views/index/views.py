from flask import render_template, request
from . import index_blu


@index_blu.route("/")
@index_blu.route("/index")
def index():
    return render_template("index.html")
