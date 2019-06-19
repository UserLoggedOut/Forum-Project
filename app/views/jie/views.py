import random

from flask import render_template, request, session

import time
from app import db
from app.models.models import User, Detail

from app.views.jie import jie_blu


@jie_blu.route("/index.html")
def index():
    return render_template("jie/index.html")


@jie_blu.route("/detail.html")
def detail():
    return render_template("jie/detail.html")


@jie_blu.route("/add.html", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        session["number1"] = random.randint(0, 9)
        session["number2"] = random.randint(0, 9)
        return render_template("jie/add.html")
    elif request.method == "POST":

        localtime = time.asctime(time.localtime(time.time()))
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        title = request.form.get("title")
        content = request.form.get("content")
        experience = request.form.get("experience")
        vercode = request.form.get("vercode")
        ss = session.get("number1") + session.get("number2")
        if int(vercode) == int(ss):
            user = db.session.query(User).filter(User.id == 1).first().detail  # 这里的1是模拟 登陆用户的id
            user_new = user[0]  # 由于查询出来的是个列表 所用要从列表中取出来 也可以用for循环取出
            user_new.title = title
            user_new.create_time = create_time
            user_new.contnet = content
            db.session.add(user_new)
            db.session.commit()
            return "验证码成功, 将数据提交到数据库中"
        return "验证码错误"


# 编辑
@jie_blu.route("/edit/<int:News_id>")
def edit(News_id):
    detail = db.session.query(Detail).filter(Detail.id == News_id).first()
    return render_template("jie/edit.html", detail=detail)





