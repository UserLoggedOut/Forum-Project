from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import APPCONFIG

# from config import DevelopmentConfig

db = SQLAlchemy()  # 创建SQLAlchemy对象时可以直接创建，后面再与flask对象进行关联


def create_app(config_name):
    # 导入创建的蓝图
    from app.views.index import index_blu
    from app.views.jie import jie_blu
    from app.views.detail import detail_blu
    from app.views.user import user_blu
    # 创建一个flask应用对象
    app = Flask(__name__)

    # app.config.from_object(DevelopmentConfig)
    app.config.from_object(APPCONFIG.get(config_name))

    # 将蓝图注册到app上
    app.register_blueprint(index_blu)
    app.register_blueprint(jie_blu, url_prefix="/jie")
    app.register_blueprint(detail_blu)
    app.register_blueprint(user_blu, url_prefix="/user")


    # 创建一个SQLAlchemy对象
    # db = )SQLAlchemy(app  # 创建SQLAlchemy对象的时候，它需要flask应用的对象，所以此时我们就可以将flask对象当做实参进行传递
    db.init_app(app)  # 如果事前SQLAlchemy对象没有进行与flask对象关联，那么此时可以完善这个操作

    return app




