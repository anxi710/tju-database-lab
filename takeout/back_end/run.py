import os
from flask import send_from_directory
from app import create_app
from app.user.models import db as user_db

app = create_app()

# 创建数据库表
with app.app_context():
    user_db.create_all()

# 提供静态文件服务，使得可以通过浏览器访问上传的文件
@app.route('/uploads/<username>/<filename>')
def uploaded_file(username, filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], username), filename)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
