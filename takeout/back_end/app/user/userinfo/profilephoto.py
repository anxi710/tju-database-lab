import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

from ...config import Config

UPLOAD_FOLDER = Config.UPLOAD_FOLDER

user_profile_photo_bp = Blueprint("user_profile_photo", __name__)

# 上传头像
@user_profile_photo_bp.route('/upload', methods=['POST'])
def upload_file():
    print("开始处理上传文件请求")

    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return jsonify({'message': '没有文件部分'}), 400

    username = request.form['userName']
    file     = request.files['file']

    print("上传的用户名为：", username)
    print("上传的文件名为：", file.filename)

    # 如果用户没有选择文件，浏览器提交的是空的文件
    if file.filename == '':
        return jsonify({'message': '没有选择文件'}), 400

    # 获取文件类型
    file_type = file.content_type.split('/')[1]

    # 获取安全的文件名
    filename = secure_filename(f'{username}/profilePhoto.{file_type}') # username 是唯一的！

    # 如果上传文件夹不存在，则创建它
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if not os.path.exists(os.path.join(UPLOAD_FOLDER, username)):
        os.makedirs(os.path.join(UPLOAD_FOLDER, username))

    # 保存文件到服务器
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # 返回保存后的文件 URL
    file_url = f'http://localhost:5000/uploads/{filename}'

    return jsonify({'url': file_url}), 200
