from flask import Blueprint, request, jsonify
from ..models import Order, Food

load_all_order_bp = Blueprint('load_all_order', __name__)

@load_all_order_bp.route('', methods=['GET'])
def load_all_order():
    print('开始加载所有订单')

    # 查询所有订单
    username = request.args.get('username')
    orders = Order.query.filter_by(username=username).all()

    order_list = []
    for order in orders:
        food = Food.query.filter_by(name = order.foodName).first()
        order_list.append({
            'shopName': food.shopName,
            'foodName': order.foodName,
            'orderPrice': order.orderPrice,
            'orderWay': order.orderWay,
            'consName': order.consName,
            'consPhone': order.consPhone,
            'consAddress': order.consAddress
        })

    return jsonify({
        'code': 200,
        'msg': '加载订单成功',
        'data': order_list
    })
