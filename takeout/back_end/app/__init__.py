from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# 创建数据库对象
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # 配置应用
    from .config import Config
    app.config.from_object(Config)

    # 初始化数据库
    db.init_app(app)

    # 注册蓝图
    from .user import user_bp
    from .shop import shop_bp
    from .order import order_bp
    app.register_blueprint(user_bp, url_prefix="/api/user", name="User")
    app.register_blueprint(shop_bp, url_prefix="/api/shop", name="Shop")
    app.register_blueprint(order_bp, url_prefix="/api/order", name="Order")

    return app
