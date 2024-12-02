from flask import Blueprint, request, jsonify
from ..models import User

user_forget_bp = Blueprint("user_forget", __name__)

# 修改密码
@user_forget_bp.route("/", methods=["POST"])
def user_forget():
    print("开始处理忘记密码请求")

    print("请求数据为：", request.json)
    telephone = request.json.get("telephone").strip()
    password = request.json.get("password").strip()

    # 使用模型进行查询
    data = User.query.filter_by(telephone=telephone).first()

    if data == None:
        print("忘记密码请求处理完成")
        return jsonify({"code": 1000, "msg": "手机号不存在"})
    else:
        data.password = password
        data.save()

        print("忘记密码请求处理完成")
        return jsonify({"code": 200, "msg": "修改成功"})
