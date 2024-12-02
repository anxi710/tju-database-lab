from flask import Blueprint, request, jsonify
from ..models import User

user_login_bp = Blueprint("user_login", __name__)

# 用户登录
@user_login_bp.route("", methods=["POST"])
def user_login():
    print(request.json)
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()

    # 使用模型进行查询
    data = User.query.filter_by(username=username, password=password).first()

    print(data)

    if data != None:
        return jsonify({"code": 200, "msg": "登录成功", "role": data.role})
    else:
        return jsonify({"code": 1000, "msg": "用户名或密码错误"})
