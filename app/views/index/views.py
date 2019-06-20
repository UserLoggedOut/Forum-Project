from flask import render_template, request, session, g

from app import db
from app.models.models import Detail, User
from app.utils.common.common import login_user_data
from . import index_blu


@index_blu.route("/")
@index_blu.route("/index")
# @login_user_data
def index():
    # 数据库查询出来

    # 查询出来detail详情个数

    # 2 取出用户登录成功存储的session数据
    user_info = session.get("user_id")
    # user_info = g.user.id
    print(user_info, "User中登录的数据")

    # 3 再次数据库查询User整个数据
    user = db.session.query(User).filter(User.id == user_info).first()
    user_detail = db.session.query(Detail).order_by(Detail.clicks.desc()).limit(8)    # 主页面
    return render_template("index.html", user=user, user_detail=user_detail)


@index_blu.route("/detail/<int:new_id>")
def details(new_id):
    # 贴吧社区详情页
    # print(new_id)
    #  1 数据库与url传参对比
    new_detail = db.session.query(Detail).filter(Detail.id == new_id).first()
    rank_detail = db.session.query(Detail).order_by(Detail.clicks.desc()).limit(8)  # 从detail数据表中查询点击最高的6个数据
    print(new_detail, "Detail对象")

    user_info2 = session.get("user_id")
    print(user_info2,"user_info2")
    # 用户
    user = db.session.query(User).filter(User.id == user_info2).first()
    print("detail", user)

    # session 存储用户发布帖子对应的id
    session["detail_id"] = new_detail.user_id
    return render_template("jie/detail.html", new_detail=new_detail, rank_detail=rank_detail, user=user)



