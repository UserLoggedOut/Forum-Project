from flask import render_template

from app.views.tiwen import tiwen_blu


@tiwen_blu.route("/tiwen")
@tiwen_blu.route("/")
def index():
    return render_template("jie/index.html")
