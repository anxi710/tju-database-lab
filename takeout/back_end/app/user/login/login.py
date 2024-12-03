from flask import Blueprint, request, jsonify
from ..models import User

user_login_bp = Blueprint("user_login", __name__)

# 用户登录
@user_login_bp.route("", methods=["POST"])
def user_login():
    print("开始处理用户登录请求")

    username = request.json.get("username").strip()
    password = request.json.get("password").strip()

    print("请求的用户名为: ", username)

    user = User.query.filter_by(username=username, password=password).first()

    if user != None:
        print("用户登录成功")
        return jsonify({"code": 200, "msg": "登录成功", "role": user.role})
    else:
        print("用户名或密码错误，拒绝登录")
        return jsonify({"code": 403, "msg": "用户名或密码错误"})
