from flask import Blueprint

shop_bp = Blueprint('shop', __name__)

# 注册子蓝图
from .loadallshop import load_all_shop_bp
from .loadshopfood import load_shop_food_bp

shop_bp.register_blueprint(load_all_shop_bp, url_prefix='/loadAllShop')
shop_bp.register_blueprint(load_shop_food_bp, url_prefix='/loadShopFood')
