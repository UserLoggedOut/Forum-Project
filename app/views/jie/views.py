import random

from flask import render_template, request, session, redirect

import time
from app import db
from app.models.models import User, Detail, Comment

from app.views.jie import jie_blu


@jie_blu.route("/index")
def index():
    return render_template("jie/index.html")


@jie_blu.route("/detail.html")
def detail():
    return render_template("jie/detail.html")


@jie_blu.route("/add.html", methods=["GET", "POST"])
def add():
    user_id = session.get("user_id")
    print(user_id, "add下的user信息")
    if not user_id:
        return redirect("/login")
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
            user = db.session.query(User).filter(User.id == user_id).first()
            # 详情数据查询
            print(user, "useruser")
            dtil = Detail()
            dtil.title = title
            dtil.content = content
            dtil.user_id = user_id
            dtil.create_time = create_time
            db.session.add(dtil)
            db.session.commit()
            # return "验证码成功, 将数据提交到数据库中"
            return redirect("index")
        return "验证码错误"


# 编辑
@jie_blu.route("/edit/<int:News_id>")
def edit(News_id):
    detail = db.session.query(Detail).filter(Detail.id == News_id).first()
    return render_template("jie/edit.html", detail=detail)


# 评论+回复
@jie_blu.route("/reply/", methods=["POST"])
def reply():
    # if request.method == "POST":
    user_info = session.get("user_id")  #
    print(user_info, "-=-=-=-=-=-=-=-=-=-=-当前登陆者 的 id")
    content = request.form.get("content")
    print(content, "-=-=-=-=-=-=-=-=-=-回复的内容")
    jid = request.form.get("jid")
    print(jid, "-=-=-=-=-=-=-=-发布新闻的id")
    if not all([user_info, content, jid]):
        return "缺少参数"
    try:
        c = Comment()
        c.detail_id = jid
        c.user_id = user_info
        c.content = content
        # if parent_id:
        #     c.parent_id = parent_id
        db.session.add(c)
        db.session.commit()
    except Exception as re:
        return "评论失败"
    return "评论成功"
