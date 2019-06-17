from flask import render_template

from app.views.user import user_blu


# 注册
@user_blu.route("/reg")
def reg():
    return render_template("user/reg.html")


# 登录
@user_blu.route("/login")
def login():
    return render_template("user/login.html")


# 忘记密码
@user_blu.route("/forget")
def forget():
    return render_template("user/forget.html")

