from . import detail_blu
from flask import render_template, request


# 创建视图函数
@detail_blu.route("/add_detail", methods=["POST", "GET"])
def add_detail():
    """社区详情编辑"""
    if request.method == "GET":
        print("aaaa")
        return render_template("jie/add.html")

    elif request.method == "POST":
        return "bbb"

