from flask import render_template, session, request

from app import db
from app.models.models import Detail, User, Comment
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

    # 3 分页
    page = request.args.get("page", 1)
    # 数据库查询
    paginate = db.session.query(Detail).paginate(int(page), 2, False)
    print(paginate)

    # 4 user数据
    details = [x.dict_detail() for x in paginate.items]
    print("存储用户里面的所有列表打印", details)

    # 3 再次数据库查询User整个数据
    user = db.session.query(User).filter(User.id == user_info).first()
    user_detail = db.session.query(Detail).order_by(Detail.clicks.desc()).limit(10)    # 主页面
    return render_template("index.html", user=user, user_detail=user_detail,
                           paginate=paginate, details=details)


@index_blu.route("/detail/<int:new_id>")
def details(new_id):
    # 贴吧社区详情页
    # print(new_id)
    #  1 数据库与url传参对比
    new_detail = db.session.query(Detail).filter(Detail.id == new_id).first()
    rank_detail = db.session.query(Detail).order_by(Detail.clicks.desc()).limit(8)  # 从detail数据表中查询点击最高的6个数据
    # print(new_detail, "Detail对象")

    user_info2 = session.get("user_id")
    # print(user_info2, "user_info2， 当前登陆者到id")
    # 用户
    user = db.session.query(User).filter(User.id == user_info2).first()
    # print("detail", user)

    # session 存储用户发布帖子对应的id
    session["detail_id"] = new_detail.user_id

    # return render_template("jie/detail.html", new_detail=new_detail, rank_detail=rank_detail, user=user)
    detail_id = db.session.query(Detail).filter(Detail.id == new_id).first()
    print(detail_id.id, '--------------------通过new_id查询出新闻的id')
    detail_author = detail_id.user  # 查询出新闻到作者
    print(detail_author.id, "-------------------查询出新闻作者的id")
    dd_content = db.session.query(Comment).filter(Comment.detail_id == detail_id.id).all()  # 当前新闻里的评论
    rr_content = db.session.query(User).filter(User.id == Comment.user_id).all()
    print(rr_content, '-----当前贴子里所用评论的用户')
    for x in rr_content:
        print(x.user_name)
    print(dd_content, '-----------------------当前帖子里所有的评论')
    for i in dd_content:
        print(i.content)
    return render_template("jie/detail.html", new_detail=new_detail,
                           rank_detail=rank_detail,
                           user=user,
                           detail_id=detail_id,
                           dd_content=dd_content,
                           rr_content=rr_content
                           )


