import os
from flask import Blueprint, request, jsonify, send_from_directory

from ...config import Config

UPLOAD_FOLDER = Config.UPLOAD_FOLDER
STATIC_FOLDER = Config.STATIC_FOLDER

user_profile_photo_bp = Blueprint("user_profile_photo", __name__)

# 上传头像
@user_profile_photo_bp.route('/upload', methods=['POST'])
def upload_file():
    print("开始处理上传头像请求")

    username = request.form['username']
    file     = request.files['file']

    file_type = file.content_type.split('/')[1]
    filename = f'new_profilePhoto.{file_type}'

    # 如果上传文件夹不存在，则创建它
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(os.path.join(UPLOAD_FOLDER, username)):
        os.makedirs(os.path.join(UPLOAD_FOLDER, username))

    # 保存文件到服务器
    file_path = os.path.join(UPLOAD_FOLDER, f'{username}', filename)
    file.save(file_path)

    print("文件保存成功")

    return jsonify({"code": 200, "msg": "上传成功"})

# 获取头像
@user_profile_photo_bp.route('/get', methods=['GET'])
def get_file():
    print("开始处理获取头像请求")

    username = request.args.get('username')

    print("获取的用户名为：", username)

    files = os.listdir(os.path.join(UPLOAD_FOLDER, username))
    for filename in files:
        if filename.startswith('profilePhoto'):
            print("用户已上传头像，返回头像")
            return send_from_directory(os.path.join(UPLOAD_FOLDER, username), filename)

    print("用户未上传头像，返回默认头像")
    return send_from_directory(STATIC_FOLDER, 'default_profile_photo.jpeg')
