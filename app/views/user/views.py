import time

from flask import render_template, request, redirect, url_for, jsonify

from app import db
from app.models.models import User

from . import user_blu


# 注册
@user_blu.route("/reg", methods=["GET", "POST"])
def reg(jsoify=None):
    if request.method == "GET":
        return render_template("user/reg.html")
    elif request.method == "POST":
        localtime = time.asctime(time.localtime(time.time()))
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("pass")
        repass = request.form.get("repass")
        vercode = request.form.get("vercode")
        print(email, username, password, repass, vercode)

        # 判断
        if password != repass:

            ret = {
                "errno": 1001,
                "errmsg": "两次密码不相同"
            }
            
            return jsonify(ret)

        # 数据库添加
        user = User()
        if user:
            user.email = email
            user.user_name = username
            user.password_hash = password
            user.create_time = create_time
            db.session.add(user)
            db.session.commit()
            return "注册成功"

        return "Aa"


# 登录
@user_blu.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("user/login.html")

    elif request.method == "POST":
        # 1 获取数据
        email = request.form.get("email")  # 邮箱
        password = request.form.get("password")

        print(email, password)

        # 2 数据库查询
        user_info = db.session.query(User).filter(User.email == email, User.password_hash == password).first()

        if user_info:
            print(user_info)
            return "aa"

        return redirect("/login")


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

