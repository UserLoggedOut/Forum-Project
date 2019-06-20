from datetime import datetime

from app import db


class Detail(db.Model):
    """贴吧详情类"""
    __tablename__ = "detail"
    id = db.Column(db.Integer, primary_key=True)  # 社区编号
    title = db.Column(db.String(256), nullable=False)  # 社区详情标题
    content = db.Column(db.String(520), nullable=False)  # 社区详情内容
    clicks = db.Column(db.Integer, default=100)  # 社区详情浏览量
    index_image_url = db.Column(db.String(256))  # 社区详情列表图片路径
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 当前用户的作者id
    user = db.relationship('User', backref=db.backref('detail', lazy='dynamic'))  # user 关联

    def dict_detail(self):

        news_dict = {
            "id": self.id,
            "title": self.title,
            "create_time": self.create_time.strftime("%Y-%m-%d"),
            "index_image_url": self.index_image_url,
            "clicks": self.clicks,
            "user_name":self.user.user_name,
            "user_id": self.user.id
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
    create_time = db.Column(db.DateTime, default=datetime.now)  # 注册时间
    signature = db.Column(db.String(512))  # 个性签名
    gender = db.Column(  # 性别
        db.Enum(
            "MAN",  # 男
            "WOMAN"  # 女
        ),
        default="MAN"
    )

    def to_dict_user(self):
        ret = {
            "id": self.id,
            "user_name": self.user_name,
            "avatar_url": self.avatar_url,
            "create_time": self.create_time,
            "signature":self.signature
        }

        return ret


#  评论类
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # 评论者id
    detail_id = db.Column(db.Integer, db.ForeignKey("detail.id"), nullable=False)  # 被评论id
    content = db.Column(db.Text, nullable=False)  # 品论内容
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录创建的时间
    parent_id = db.Column(db.Integer, db.ForeignKey("comment.id"))  # 父品论id
    parent = db.relationship("Comment", remote_side=id)  # 自关联

    def to_basic_dict(self):
        ret = {
            'id': self.id,
            'user_id': self.user_id,
            'detail_id': self.detail_id,
            'user_avatar_url': self.user.avatar_url,  # 用户头像
            'user_name': self.user.user_name,  # 用户名
            'create_time': self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            'prent': self.prent.to_basic_dict()if self.parent else None,
        }
        return ret

