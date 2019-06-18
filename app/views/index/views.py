from flask import render_template, request

from app.models.models import User
from . import index_blu


@index_blu.route("/")
@index_blu.route("/index")
def index():
    # 主页面
    return render_template("index.html")


@index_blu.route("/detail")
def detail():
    # 贴吧社区详情页
    return render_template("jie/detail.html")

