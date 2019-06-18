from flask import render_template, request, redirect, url_for

from app.models.models import User
from app.views.user import user_blu


# 注册
@user_blu.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("user/reg.html")
    elif request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("pass")
        repass = request.form.get("repass")
        vercode = request.form.get("vercode")
        # if not password == repass:
        #     print(4444)
        #     # 如果密码不正确就返回一个新的页面
        #     return redirect(url_for(''))






# 登录
@user_blu.route("/login")
def login():
    return render_template("user/login.html")


# 忘记密码
@user_blu.route("/forget")
def forget():
    return render_template("user/forget.html")


# 主页
@user_blu.route("/home")
def home():
    return render_template("user/home.html")


# 用户中心
@user_blu.route("/index")
def index():
    return render_template("user/index.html")


# 基本设置
@user_blu.route("/set")
def set():
    return render_template("user/set.html")


# 我的消息
@user_blu.route("/message")
def message():
    return render_template("user/message.html")


# 邮箱激活
@user_blu.route("/activate")
def activate():
    return render_template("user/activate.html")

