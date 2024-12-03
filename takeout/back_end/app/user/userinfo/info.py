import os
from flask import Blueprint, request, jsonify

from ..models import User
from ...config import Config

UPLOAD_FOLDER = Config.UPLOAD_FOLDER

user_info_bp = Blueprint("user_info", __name__)

@user_info_bp.route("", methods=["GET"])
def user_info():
    print("开始处理获取用户信息请求")

    username = request.args.get("username")
    print("请求的用户名为：", username)

    data = User.query.filter_by(username=username).first()

    if data != None:
        # 查找 uploads/<username> 文件夹下，不带后缀名称为 profilePhoto 的文件
        profilePhoto = None
        if os.path.exists(os.path.join(UPLOAD_FOLDER, username)):
            for file in os.listdir(os.path.join(UPLOAD_FOLDER, username)):
                if file.split('.')[0] == 'profilePhoto':
                    profilePhoto = f'{file}'
                    break

        profilePhotoUrl = f'http://localhost:5000/uploads/{username}/{profilePhoto}' if profilePhoto != None else None

        return jsonify({
            "code": 200,
            "msg": "获取成功",
            "data": {
                "profilePhotoUrl": profilePhotoUrl,
                "sex": data.sex,
                "realName": data.realname,
                "telephone": data.telephone,
            }
        })