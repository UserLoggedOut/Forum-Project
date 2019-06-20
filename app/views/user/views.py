import random
import time

from flask import render_template, request, redirect, url_for, jsonify, session

from app import db
from app.models.models import User, Detail

from . import user_blu


# 注册
@user_blu.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        session["num1"] = random.randint(0, 9)
        session["num2"] = random.randint(0, 9)
        return render_template("user/reg.html")
    elif request.method == "POST":
        localtime = time.asctime(time.localtime(time.time()))
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 注册的时间
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("pass")
        repass = request.form.get("repass")
        vercode = request.form.get("vercode")
        ss = session.get("num1") + session.get("num2")
        # print(email, username, password, repass, vercode)
        # print(ss, '-----人类验证码')
        print(type(email), email)
        # 判断
        user = db.session.query(User).filter(User.email == email).first()
        print(user, "通过邮箱查找出相同用户")
        if len(password) >= 6:
            print('-----------1--------------------')
            if password != repass:
                ret = {
                    "errno": 1001,
                    "errmsg": "两次密码不相同"
                }
                return jsonify(ret)
            else:
                # 数据库添加
                if int(vercode) == int(ss):
                    user = User()
                    if user:
                        print('-----------2--------------------')
                        # 用户注册成功
                        try:
                            user.email = email
                            user.user_name = username
                            user.password_hash = password
                            user.create_time = create_time
                            db.session.add(user)
                            db.session.commit()
                        except Exception as re:
                            return "注册失败,邮箱已被注册"
                        # 2 重定向到index
                        return redirect("/login")
                    return "Aa"
                return "验证码错误，或邮箱以被注册"
        return "密码格式不对"


# 登录
@user_blu.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        session["n1"] = random.randint(0, 9)
        session["n2"] = random.randint(0, 9)
        return render_template("user/login.html")

    elif request.method == "POST":
        # 1 获取数据
        email = request.form.get("email")  # 邮箱
        password = request.form.get("password")
        vercode = request.form.get("vercode")
        ss = session.get("n1") + session.get("n2")
        print(email, password, vercode, ss)
        if int(vercode) == int(ss):
            # 2 数据库查询
            user_info = db.session.query(User).filter(User.email == email, User.password_hash == password).first()
            if user_info:
                # 如果验证用户登录成功
                # 1 通过session存储用户的信息
                session["user_id"] = user_info.id

                # 2 js 异常 使用重定向到index主义
                return redirect("/index")

            # 如果用户未登录成功再次跳转到登录页面
            return redirect("/login")
        return "人机验证码错误"

# 退出
@user_blu.route("/logout")
def logout():
    # 退出清除session 标记
    session.clear()
    print("退出清除session成功")

    # 2 返回主页
    return redirect("/index")


# 忘记密码
@user_blu.route("/forget", methods=["POST", "GET"])
def forget():
    if request.method == "GET":
        return render_template("user/forget.html")
    elif request.method == "POST":
        # 1 获取参数
        email = request.form.get("email")
        print(email)
        # 数据库查询
        user_email = db.session.query(User).filter(User.email == email).first()
        print(user_email, "查询用户的email是否有对应")
        if user_email:
            # 如果查询到了用户输入的邮箱与查询出来的邮箱成立就执行下面的事情

            # 1 通过session存储email
            session["user_email"] = user_email.email  # 邮箱

            email_user = session.get("user_email")
            print(email_user, "email_user")

            # 2 邮箱验证
            # 通过hashlib相关功能得到一个随机值，这个 随机值出现可能性的概率几乎为0
            mail_hash = hashlib.md5()
            mail_hash.update(str(time.time()).encode("utf-8"))
            email_hash_value = mail_hash.hexdigest()

            # 制作一个url，用来发送到电子邮箱中，从而才能让用户点击
            # http://localhost:5000/verify_email?email_hash=aksdjflasjdflkjaskldfjlasdjflksjdf
            verify_email_url = request.host_url + "forget3?user_email=" + email_user

            # sender发信人  recipients收信人
            msg = Message('欢迎来到Fly社区，请验证', sender='13030119817@163.com', recipients=[email])
            msg.body = '你好'
            msg.html = "你好，点击<a href=%s >修改密码</a>, 如有问题请联系Fly社区管理员" % verify_email_url
            mail.send(msg)

            # 返回
            return "邮箱验证发送成功点击<a href=https://mail.163.com/>登录</a>邮箱验证"

        else:
            return "邮箱不存在"


@user_blu.route("/forget3", methods=["POST", "GET"])
def forget3():
    """忘记密码"""
    if request.method == "GET":
        return render_template("user/forgetPwd3.html")

    elif request.method == "POST":
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user_email = session.get("user_email")  # 用户输入的忘记密码的邮箱
        print(password1, password2, user_email)

        # 查询出当前改密码的用户是否与数据库相同
        new_user = db.session.query(User).filter(User.email == user_email).first()
        # 判断
        if new_user:
            if not (password1 and password2):
                return "缺少参数 点击<a href=/forget3>返回</a>"
            if password1 != password2:
                return "两次密码不一致 点击<a href=/forget3>返回</a>"
            if password1 == password2:
                # print(new_user.password)
                new_user.password_hash = password1
                # 提交
                db.session.commit()

            return redirect(url_for(".forget_pwd4"))
        return "不能重新修改密码谢谢 点击<a href=/login>返回</a>"


@user_blu.route("/forget_pwd4")
def forget_pwd4():
    session.clear()  # 清除session 用户只能在验证通过后修改一次密码
    return render_template("user/forgetPwd4.html")


# 主页
@user_blu.route("/home")
def home():
    user_id = session.get("user_id")
    user = db.session.query(User).filter(User.id == user_id).first()
    return render_template("user/home.html", user=user)


# 用户中心
@user_blu.route("/index")
def index():
    aaa = db.session.query(Detail).all()
    return render_template("user/index.html", aaa=aaa)


# 基本设置
@user_blu.route("/set", methods=["GET", "POST"])
def set():
    # 1.获取用户id
    user_id = session.get("user_id")
    # 2.查询数据库
    user = db.session.query(User).filter(User.id == user_id).first()
    if request.method == "GET":
        return render_template("user/set.html", user=user)
    elif request.method == "POST":
        # 获取信息
        email = request.form.get("email")
        username = request.form.get("username")
        sex = request.form.get("sex")
        # city = request.form.get("city")
        sign = request.form.get("sign")
        nowpass = request.form.get("nowpass")
        passs = request.form.get("pass")
        repass = request.form.get("repass")
        if email:
            # 修改用户信息
            user.email = email
            user.user_name = username
            user.gender = sex
            user.signature = sign

        if user.password_hash == nowpass:
            if passs == repass:
                user.password_hash = passs
        # 提交信息
        db.session.commit()
        return "修改成功"


@user_blu.route("/upload/", methods=["POST"])
@user_blu.route("/user/upload/", methods=["POST"])
def upload():
    # 获取登录用户的id
    user_id = session.get("user_id")
    # # 从数据库中查询这个用户
    user = db.session.query(User).filter(User.id == user_id).first()
    # return render_template("user/set.html", user=user)
    # 1.获取信息
    binary = request.files.get("binary")
    print(binary)
    # return "1234"
    file = request.files.get("file")
    print(file)
    # 2.判断
    if file:
        file_hash = hashlib.md5()
        file_hash.update(file.filename.encode("utf-8"))
        file_name = file_hash.hexdigest() + file.filename[file.filename.rfind("."):]
        local_file_path = os.path.join("/static/upload/images", file_name)

        file_path = os.path.join(current_app.root_path, "static/upload/images", file_name)

        file.save(file_path)

        user.avatar_url = local_file_path
        db.session.commit()
        return "成功"
    else:
        return "出错了"


# 我的消息
@user_blu.route("/message")
def message():
    return render_template("user/message.html")


# 邮箱激活
@user_blu.route("/activate")
def activate():
    return render_template("user/activate.html")

