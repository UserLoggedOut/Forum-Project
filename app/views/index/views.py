from flask import render_template, request, session

from app import db
from app.models.models import Detail, User
from . import index_blu


@index_blu.route("/")
@index_blu.route("/index")
def index():
    # 数据库查询出来
    user = db.session.query(User).first()
    # 查询出来detail详情个数
    user_detail = db.session.query(Detail).order_by(Detail.clicks.desc()).limit(5)    # 主页面
    return render_template("index.html", user=user, user_detail=user_detail)


@index_blu.route("/detail/<int:new_id>")
def details(new_id):
    # 贴吧社区详情页
    # print(new_id)
    #  1 数据库与url传参对比
    new_detail = db.session.query(Detail).filter(Detail.id == new_id).first()
    rank_detail = db.session.query(Detail).order_by(Detail.clicks.desc()).limit(5)  # 从detail数据表中查询点击最高的6个数据
    print(new_detail, "Detail对象")

    # session 存储用户发布帖子对应的id
    session["detail_id"] = new_detail.user_id
    return render_template("jie/detail.html", new_detail=new_detail, rank_detail=rank_detail)

