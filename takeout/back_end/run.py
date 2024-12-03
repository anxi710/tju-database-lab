from app import create_app
from app.user.models import db as user_db

app = create_app()

# 创建数据库表
with app.app_context():
    user_db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
