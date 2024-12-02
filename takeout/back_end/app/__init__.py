from flask import Flask
from flask_cors import CORS
from .config import Config
from .user import user_bp
from .user.models import db as user_db

def create_app():
    app = Flask(__name__)
    CORS(app)

    # 配置应用
    app.config.from_object(Config)
    app.register_blueprint(user_bp)

    # 初始化数据库
    user_db.init_app(app)

    # 注册蓝图
    app.register_blueprint(user_bp, url_prefix="/api/user", name="User")

    return app
