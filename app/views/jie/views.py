from flask import render_template

from app.views.jie import tiwen_blu


@tiwen_blu.route("/index")
def index():
    return render_template("jie/index.html")


@tiwen_blu.route("/detail.html")
def detail():
    return render_template("jie/detail.html")


@tiwen_blu.route("/add.html")
def add():
    return render_template("jie/add.html")


