from flask import render_template

from app.views.user import user_blu


@user_blu.route("/reg")
def reg():
    return render_template("user/reg.html")


