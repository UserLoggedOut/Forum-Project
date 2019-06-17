from flask import render_template

from app.views.jie import tiwen_blu


@tiwen_blu.route("/index")
def index():
    return render_template("jie/index.html")
