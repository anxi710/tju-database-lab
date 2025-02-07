import os
from flask import Blueprint, request, jsonify

from ..models import User

user_info_bp = Blueprint("user_info", __name__)

@user_info_bp.route("/get", methods=["GET"])
def user_info():
    print("开始处理获取用户信息请求")

    username = request.args.get("username")
    print("请求的用户名为：", username)

    data = User.query.filter_by(username=username).first()

    if data != None:

        return jsonify({
            "code": 200,
            "msg": "获取成功",
            "data": {
                "username": username,
                "sex": data.sex,
                "realname": data.realname,
                "telephone": data.telephone,
            }
        })

@user_info_bp.route("/update", methods=["POST"])
def update_user_info():
    print("开始处理更新用户信息请求")

    username = request.json.get("username")
    print("请求的用户名为：", username)

    user = User.query.filter_by(username=username).first()

    if user != None:
        user.realname  = request.json.get("realname")
        user.sex       = request.json.get("sex")
        user.save()

        return jsonify({"code": 200, "msg": "更新成功"})
    else:
        return jsonify({"code": 400, "msg": "用户不存在"})
