from flask import Blueprint, request, jsonify
from ..models import Shop, Food

load_shop_food_bp = Blueprint("load_shop_food", __name__)

@load_shop_food_bp.route("", methods=["GET"])
def load_shop_food():
    print("开始处理加载商店食物请求")

    shopName = request.args.get("shopName")
    print("请求的商店名为：", shopName)

    if shopName == None:
        return jsonify({"code": 400, "msg": "请求参数错误"})
    elif Shop.query.filter_by(name=shopName).first() == None:
        return jsonify({"code": 400, "msg": "商店不存在"})

    data = Food.query.filter_by(shopName=shopName)

    foodList = []
    if data != None:
        for food in data:
            foodList.append({
                "name": food.name,
                "price": food.price,
                "image": food.image
            })

    return jsonify({
        "code": 200,
        "msg": "获取成功",
        "data": foodList
    })
