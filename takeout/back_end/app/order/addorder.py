from flask import Blueprint, jsonify, request
from ..models import Order

add_order_bp = Blueprint('add_order', __name__)

@add_order_bp.route('', methods=['POST'])
def add_order():
    print('开始处理添加订单请求')

    # 获取请求数据
    username = request.json.get('username')
    foodName = request.json.get('foodName')
    orderPrice = request.json.get('orderPrice')
    orderWay = request.json.get('orderWay')
    consName = request.json.get('consName')
    consPhone = request.json.get('consPhone')
    consAddress = request.json.get('consAddress')

    Order(
        username=username,
        foodName=foodName,
        orderPrice=orderPrice,
        orderWay=orderWay,
        consName=consName,
        consPhone=consPhone,
        consAddress=consAddress
    ).save()

    return jsonify({'code': 200, 'msg': '添加成功'})