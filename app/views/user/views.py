import random
import time

from flask import render_template, request, redirect, url_for, jsonify, session

from app import db
from app.models.models import User

from . import user_blu


# 注册
@user_blu.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        session["num1"] = random.randint(0, 9)
        session["num2"] = random.randint(0, 9)
        return render_template("user/reg.html")
    elif request.method == "POST":
        localtime = time.asctime(time.localtime(time.time()))
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 注册的时间
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("pass")
        repass = request.form.get("repass")
        vercode = request.form.get("vercode")
        ss = session.get("num1") + session.get("num2")
        print(email, username, password, repass, vercode)
        print(ss, '-----人类验证码')

        # session 存

        # 判断
        #
        # if password != repass:
        #     ret = {
        #         "errno": 1001,
        #         "errmsg": "两次密码不相同"
        #     }
        #
        #     return jsonify(ret)

        # 数据库添加
        if int(vercode) == int(ss):
            user = User()
            if user:
                # 用户注册成功
                user.email = email
                user.user_name = username
                user.password_hash = password
                user.create_time = create_time
                db.session.add(user)
                db.session.commit()
                # 2 重定向到index
                return redirect("/login")

            return "Aa"
        return "验证码错误"


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
            # 如果验证用户登录成功

            # 1 通过session存储用户的信息
            session["user_id"] = user_info.id

            # 2 js 异常 使用重定向到index主义
            return redirect("/index")

        # 如果用户未登录成功再次跳转到登录页面
        return redirect("/login")


# 退出
@user_blu.route("/logout")
def logout():
    # 退出清除session 标记
    session.clear()
    print("退出清除session成功")

    # 2 返回主页
    return redirect("/index")


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

