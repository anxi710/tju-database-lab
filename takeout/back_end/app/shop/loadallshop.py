from flask import Blueprint, jsonify
from ..models import Shop

load_all_shop_bp = Blueprint("load_all_shop", __name__)

@load_all_shop_bp.route("", methods=["GET"])
def load_all_shop():
    print("开始处理加载所有商店请求")

    data = Shop.query.all()

    shopList = []
    for shop in data:
        shopList.append({
            "name": shop.name,
            "address": shop.address,
        })

    return jsonify({
        "code": 200,
        "msg": "获取成功",
        "data": shopList
    })
