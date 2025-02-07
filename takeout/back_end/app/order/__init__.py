from flask import Blueprint

order_bp = Blueprint('order', __name__)

# 注册子蓝图
from .addorder import add_order_bp
order_bp.register_blueprint(add_order_bp, url_prefix='/addOrder')

from .loadallorder import load_all_order_bp
order_bp.register_blueprint(load_all_order_bp, url_prefix='/loadAllOrder')
