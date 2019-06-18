from flask import Blueprint

# 创建蓝图
detail_blu = Blueprint("detail_blu", __name__)

from . import views
