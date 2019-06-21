import random

from app import db
from app.models.models import Detail
from app.utils.common.common import login_user_data
from . import detail_blu
from flask import render_template, request, session, redirect, url_for,g


# 创建视图函数
@detail_blu.route("/add_detail/<news_id>", methods=["POST", "GET"])
@login_user_data
def add_detail(news_id):
    """社区详情编辑"""

    detail_id = db.session.query(Detail).filter(Detail.id == news_id).first()
    print(detail_id)

    user = g.user
    if not user:
        return redirect("/login")
    if request.method == "GET":
        # session["number1"] = random.randint(0, 9)
        # session["number2"] = random.randint(0, 9)
        print("add.html", user)
        return render_template("jie/add.html", detail_id=detail_id, user=g.user)

    elif request.method == "POST":
        title = request.form.get("title")  # 编辑标题
        content = request.form.get("content")  # 编辑内容

        print(title, content, "333")
        # ss = session.get("number1") + session.get("number2")

        # 数据库修改
        detail_id.title = title  # 标题
        detail_id.content = content  # 内容
        db.session.commit()

        return redirect("/index")

