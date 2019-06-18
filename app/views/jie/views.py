import random

from flask import render_template, request, session

from app.views.jie import tiwen_blu


@tiwen_blu.route("/index")
def index():
    return render_template("jie/index.html")


@tiwen_blu.route("/detail.html")
def detail():
    return render_template("jie/detail.html")


@tiwen_blu.route("/add.html", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        session["number1"] = random.randint(0, 9)
        session["number2"] = random.randint(0, 9)
        return render_template("jie/add.html")
    elif request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        experience = request.form.get("experience")
        vercode = request.form.get("vercode")
        ss = session.get("number1") + session.get("number2")
        print(ss, vercode)
        if int(vercode) == int(ss):
            print(vercode, "vercode+++===")
            return "验证码成功"
        return "验证码错误"

