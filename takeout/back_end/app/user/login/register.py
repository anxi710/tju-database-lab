from flask import Blueprint, request, jsonify
from ...models import User

user_register_bp = Blueprint("user_register", __name__)

# 用户注册
@user_register_bp.route("", methods=["POST"])
def user_register():
    print("开始处理注册请求")

    username  = request.json.get("username").strip()
    password  = request.json.get("password").strip()
    telephone = request.json.get("telephone").strip()
    role      = "user"  # 从客户端发起的创建用户请求默认为普通用户

    data1 = User.query.filter_by(username=username).first()
    data2 = User.query.filter_by(telephone=telephone).first()

    if data1 != None:
        print("注册请求处理完成")
        return jsonify({"code": 403, "msg": "用户名已存在"})
    elif data2 != None:
        print("注册请求处理完成")
        return jsonify({"code": 403, "msg": "手机号已注册"})
    else:
        user = User(username=username, password=password, telephone=telephone, role=role)
        # 将新用户信息添加到数据库
        user.save()

        print("注册请求处理完成")
        return jsonify({"code": 200, "msg": "注册成功"})
