from datetime import datetime

from app import db


class Detail(db.Model):
    """贴吧详情类"""
    __tablename__ = "detail"
    id = db.Column(db.Integer, primary_key=True)  # 社区编号
    title = db.Column(db.String(256), nullable=False)  # 社区详情标题
    source = db.Column(db.String(64), nullable=False)  # 社区详情来源
    digest = db.Column(db.String(512), nullable=False)  # 社区详情摘要
    content = db.Column(db.Text, nullable=False)  # 社区详情内容
    clicks = db.Column(db.Integer, default=0)  # 社区详情浏览量
    index_image_url = db.Column(db.String(256))  # 社区详情列表图片路径
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 当前用户的作者id
    user = db.relationship('User', backref=db.backref('detail', lazy='dynamic'))  # user 关联

    def dict_detail(self):

        news_dict = {
            "id": self.id,
            "title": self.title,
            "source": self.source,
            "digest": self.digest,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "index_image_url": self.index_image_url,
            "clicks": self.clicks
        }
        return news_dict


class User(db.Model):
    """用户表"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)  # id
    email = db.Column(db.String(32), unique=True, nullable=False)
    user_name = db.Column(db.String(32), unique=True, nullable=False)  # 名字 unique 不能出现重复
    avatar_url = db.Column(db.String(256))  # 用户头像路径
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    create_time = db.Column(db.DateTime)  # 注册时间
    signature = db.Column(db.String(512), default=datetime.now)  # 个性签名
    gender = db.Column(  # 性别
        db.Enum(
            "MAN",  # 男
            "WOMAN"  # 女
        ),
        default="MAN"
    )

    def to_dict_user(self):
        ret = {
            "id":self.id,
            "user_name":self.user_name,
            "avatar_url": self.avatar_url
        }

        return ret

    # followers = db.relationship('User',
    #                             secondary=Follow.__tablename__,
    #                             primaryjoin=(id == Follow.followed_id),
    #                             secondaryjoin=(id == Follow.follower_id),
    #                             backref=db.backref('followed', lazy='dynamic'),
    #                             lazy='dynamic')


