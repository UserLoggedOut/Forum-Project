from app import db
from app.models.models import Detail
from . import detail_blu
from flask import render_template, request, session, redirect, url_for


# 创建视图函数
@detail_blu.route("/add_detail/<news_id>", methods=["POST", "GET"])
def add_detail(news_id):
    """社区详情编辑"""

    detail_id = db.session.query(Detail).filter(Detail.id == news_id).first()
    print(detail_id)

    if request.method == "GET":
        # print("aaaa")
        # detail_id = session.get("detail_id")
        # print(detail_id, "session 存储的数据")
        return render_template("jie/add.html", detail_id=detail_id)

    elif request.method == "POST":
        title = request.form.get("title")  # 编辑标题
        content = request.form.get("content")  # 编辑内容

        print(title, content, "333")

        # 数据库修改
        detail_id.title = title  # 标题
        detail_id.content = content  # 内容
        db.session.commit()

        return redirect("/index")

