# import caching as caching
import os
from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
from sqlalchemy import text

from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
import auth
import datetime

# 跨域
from flask_cors import cross_origin

app = Flask(__name__)

# 添加配置数据库
app.config.from_object(BaseConfig)
# 初始化拓展，app 到数据库的 ORM 映射
db = SQLAlchemy(app)

# 检查数据库连接是否成功
with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())

# 上传文件的保存目录
UPLOAD_FOLDER = 'uploads'

# 配置 Flask 上传目录
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 用户登录
@app.route("/api/user/login", methods=["POST"])
@cross_origin()
def user_login():
    print(request.json)
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()

    sql = f'select * from user where username = "{username}" and password = "{password}"'

    data = db.session.execute(text(sql)).first()

    print(data)

    if data != None:
        user = {'uid': data[0], 'username': data[1], 'telephone': data[2],
                'password': data[3], 'role': data[4]}

        print("user info: ", user)

        return jsonify({"code": 200, "msg": "登录成功", "role": data[4]})
    else:
        return jsonify({"code": 1000, "msg": "用户名或密码错误"})

# 用户注册
@app.route("/api/user/register", methods=["POST"])
@cross_origin()
def user_register():
    print("开始处理注册请求")

    print("请求数据为：", request.json)
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    telephone = request.json.get("telephone").strip()
    role = request.json.get("role").strip()

    sql1 = f'SELECT * FROM user WHERE username = "{username}"'
    sql2 = f'SELECT * FROM user WHERE telephone = "{telephone}"'

    data1 = db.session.execute(text(sql1)).first()
    data2 = db.session.execute(text(sql2)).first()

    print(data1)
    print(data2)

    if data1 != None:
        print("注册请求处理完成")
        return jsonify({"code": 1000, "msg": "用户名已存在"})
    elif data2 != None:
        print("注册请求处理完成")
        return jsonify({"code": 1000, "msg": "手机号已注册"})
    else:
        sql = f'INSERT INTO user(username, telephone, password, role) VALUES ("{username}", "{telephone}", "{password}", "{role}")'
        db.session.execute(text(sql))
        db.session.commit()
        print("注册请求处理完成")
        return jsonify({"code": 200, "msg": "注册成功"})

# 修改密码
@app.route("/api/user/forget", methods=["POST"])
@cross_origin()
def user_forget():
    print("开始处理忘记密码请求")

    print("请求数据为：", request.json)
    telephone = request.json.get("telephone").strip()
    password = request.json.get("password").strip()

    # 判断手机号是否存在
    sql = f'SELECT * FROM user WHERE telephone = "{telephone}"'
    data = db.session.execute(text(sql)).first()

    if data == None:
        print("忘记密码请求处理完成")
        return jsonify({"code": 1000, "msg": "手机号不存在"})

    sql = f'UPDATE user SET password = "{password}" WHERE telephone = "{telephone}"'

    db.session.execute(text(sql))
    db.session.commit()
    print("忘记密码请求处理完成")
    return jsonify({"code": 200, "msg": "修改成功"})

# 上传头像
@app.route('/api/user/upload', methods=['POST'])
@cross_origin()
def upload_file():
    print("开始处理上传文件请求")
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return jsonify({'message': '没有文件部分'}), 400

    file = request.files['file']

    # 如果用户没有选择文件，浏览器提交的是空的文件
    if file.filename == '':
        return jsonify({'message': '没有选择文件'}), 400

    # 获取文件类型
    file_type = file.content_type.split('/')[1]

    # 获取安全的文件名
    filename = secure_filename(f'profilePhoto.{file_type}') # username 是唯一的！

    # 如果上传文件夹不存在，则创建它
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # 保存文件到服务器
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # 返回保存后的文件 URL
    file_url = f'http://localhost:5000/uploads/{filename}'

    return jsonify({'url': file_url}), 200

# 提供静态文件服务，使得可以通过浏览器访问上传的文件
@app.route('/uploads/<filename>')
@cross_origin()
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# 用户界面获取店铺信息
@app.route("/api/user/shop", methods=["GET"])
@cross_origin()
def user_get_shop():
    data = db.session.execute(text('select * from fastfood_shop')).fetchall()

    Data = []
    for i in range(len(data)):
        dic = dict(shop_name=data[i][0], price=data[i][1], sale=data[i][2])
        Data.append(dic)
    print(Data)
    # return jsonify({"status":"200", "tabledata": Data})
    return jsonify(status=200, tabledata=Data)

# 下订单
@app.route("/api/user/addorder", methods=["POST"])
@cross_origin()
def user_addorder():
    rq = request.json
    # 获取各个参数
    shopname = rq.get("shop_name")
    ordermoney = rq.get("order_money")
    orderway = rq.get("order_way")
    consphone = get_token_phone(request.headers.get('token'))
    consname = rq.get("cons_name")
    consaddre = rq.get("cons_addre")
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # print(shop_name, order_money, order_way, cons_phone, cons_name, cons_addre)
    db.session.execute(text( 'insert into oorder( shop_name, order_money, order_way, cons_phone, cons_name, cons_addre,create_time) value("%s", %d, "%s", "%s", "%s", "%s","%s")' % (
            shopname, ordermoney, orderway, consphone, consname, consaddre, create_time)))
    db.session.commit()
    # db.session.execute('insert into fastfood_shop(shop_name, price, m_sale_v) values("解耦哎",10,100)')
    # db.session.commit()
    return jsonify(status=200, msg="成功下单")


def get_token_phone(token):
    data = auth.decode_func(token)
    phone = data['telephone']
    return (phone)


@app.route("/api/user/unsend", methods=["POST", "GET", "DELETE"])
@cross_origin()
def user_unsend():
    if request.method == 'GET':
        phone = get_token_phone(request.headers.get('token'))
        print(phone)
        data = db.session.execute(text('select * from oorder where checked=0 and cons_phone="%s"' % phone)).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(order_id=data[i][0], shop_name=data[i][1], price=data[i][2], orderway=data[i][3],
                       cons_name=data[i][5], cons_addre=data[i][6], create_time=data[i][8])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)
    if request.method == 'POST':
        rq = request.json
        order_id = rq.get("order_id")
        cons_name = rq.get("cons_name")
        cons_addre = rq.get("cons_addre")
        print(order_id)
        db.session.execute(
            text('update oorder set cons_name="%s", cons_addre="%s" where order_id="%d"' % (cons_name, cons_addre, order_id)))
        db.session.commit()
        return jsonify(status=200, msg="修改成功")
    if request.method == 'DELETE':
        order_id = request.json.get("delete_id")
        db.session.execute(text('delete from oorder where order_id="%d" ' % order_id))
        db.session.commit()
        return jsonify(status=200, msg="删除成功")


@app.route("/api/user/sending", methods=["POST", "GET", "DELETE"])
@cross_origin()
def user_sending():
    if request.method == 'GET':
        phone = get_token_phone(request.headers.get('token'))

        data = db.session.execute(text('select * from sending_order where cons_phone="%s"' % phone)).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(order_id=data[i][0], shop_name=data[i][1], order_money=data[i][2], order_way=data[i][3],
                       cons_phone=data[i][4],
                       cons_name=data[i][5], cons_addre=data[i][6], disp_id=data[i][7], deliver_time=data[i][8],
                       disp_phone=data[i][9])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)


@app.route("/api/user/sended", methods=["POST", "GET", "DELETE"])
@cross_origin()
def user_sended():
    if request.method == 'GET':
        phone = get_token_phone(request.headers.get('token'))
        data = db.session.execute(text('select * from sended_order where cons_phone="%s"' % phone)).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(order_id=data[i][0], shop_name=data[i][1], order_money=data[i][2], order_way=data[i][3],
                       cons_phone=data[i][4],
                       cons_name=data[i][5], cons_addre=data[i][6], disp_id=data[i][7], deliver_time=data[i][8],
                       disp_phone=data[i][9])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)


@app.route("/api/user/usermsg", methods=["POST", "GET"])
@cross_origin()
def usermsg():
    if request.method == 'GET':
        phone = get_token_phone(request.headers.get('token'))
        data = db.session.execute(text('select * from user_msg where phone="%s"' % phone)).fetchall()
        Data = dict(real_name=data[0][1], sex=data[0][2], age=data[0][3], mail=data[0][4], phone=data[0][5],
                   user_name=data[0][6])

        return jsonify(status=200, data=Data)


@app.route("/api/user/pwd_chg", methods=["POST"])
@cross_origin()
def user_pwd_chg():
    if request.method=='POST':
        pwd=request.json.get('new_pwd')
        old_pwd=request.json.get('old_pwd')
        phone = get_token_phone(request.headers.get('token'))
        data = db.session.execute(text('select * from user where telephone="%s" and password="%s"'% (phone,old_pwd))).fetchall()
        if not data:
            return jsonify(status=1000,msg="原始密码错误")
        else:
            db.session.execute(text('update user set password="%s" where telephone="%s"'% (pwd,phone)))
            db.session.commit()
            return jsonify(status=200,msg="修改成功")


@app.route("/api/manager/shop", methods=["POST", "GET", "DELETE"])
@cross_origin()
def manager_shop():
    # 获取店铺信息
    if request.method == 'GET':
        data = db.session.execute(text('select * from fastfood_shop')).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(shop_name=data[i][0], price=data[i][1], sale=data[i][2])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)
    if request.method == 'POST' and request.json.get('action') == "add":
        rq = request.json
        shop_name = rq.get('shop_name')
        price = rq.get('price')
        m_sale_v = rq.get('m_sale_v')
        exist = db.session.execute(text('select * from fastfood_shop where shop_name="%s"' % shop_name)).fetchall()
        if not exist:
            db.session.execute(text('insert fastfood_shop(shop_name,price,m_sale_v) value("%s",%d,%d)' % (
                shop_name, int(price), int(m_sale_v))))
            db.session.commit()
            return jsonify(status=200, msg="添加成功")
        else:
            return jsonify(status=1000, msg="该店铺已存在")

    if request.method == 'POST' and request.json.get('action') == "change":
        rq = request.json
        shop_name = rq.get('shop_name')
        price = rq.get('price')
        m_sale_v = rq.get('m_sale_v')
        db.session.execute(text('update fastfood_shop set price="%d", m_sale_v="%d" where shop_name="%s" ' % (
            int(price), int(m_sale_v), shop_name)))
        db.session.commit()
        return jsonify(status=200, msg="修改成功")
    if request.method == 'DELETE':
        want_delete = request.json.get('want_delete')
        db.session.execute(text('delete from fastfood_shop where shop_name="%s"' % want_delete))
        db.session.commit()
        return jsonify(status=200, msg="删除成功")


@app.route("/api/manager/server", methods=["POST", "GET", "DELETE"])
@cross_origin()
def manager_server():
    if request.method == 'GET':
        data = db.session.execute(text('select * from server')).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(service_id=data[i][0], service_name=data[i][1], fastfood_shop_name=data[i][2])
            Data.append(dic)
        shop_range = db.session.execute(text('select shop_name from fastfood_shop')).fetchall()
        Shop = []
        for i in range(len(shop_range)):
            dic = dict(shop_name=shop_range[i][0])
            Shop.append(dic)
        print(Shop)
        return jsonify(status=200, tabledata=Data, shop_range=Shop)
    if request.method == 'POST':
        rq = request.json
        service_id = rq.get('service_id')
        service_name = rq.get('service_name')
        fastfood_shop_name = rq.get('fastfood_shop_name')
        exist = db.session.execute(text('select * from server where service_id="%s"' % service_id)).fetchall()
        if not exist:
            db.session.execute(text('insert server(service_id,service_name,fastfood_shop_name) value("%s","%s","%s")' % (
                service_id, service_name, fastfood_shop_name)))
            db.session.commit()
            return jsonify(status=200, msg="添加成功")
        else:
            return jsonify(status=1000, msg="该编号已存在")
    if request.method == 'DELETE':
        want_delete = request.json.get('want_delete')
        db.session.execute(text('delete from server where service_id="%s"' % want_delete))
        db.session.commit()
        return jsonify(status=200, msg="解雇成功")


@app.route("/api/manager/dispatcher", methods=["POST", "GET", "DELETE"])
@cross_origin()
def manager_dispatcher():
    if request.method == 'GET':
        data = db.session.execute(text('select * from dispatcher')).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(dispatcher_id=data[i][0], dispatcher_name=data[i][1], dispatcher_phone=data[i][2])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)
    if request.method == 'POST':
        rq = request.json
        dispatcher_id = rq.get('dispatcher_id')
        dispatcher_name = rq.get('dispatcher_name')
        dispatcher_phone = rq.get('dispatcher_phone')
        exist = db.session.execute(text('select * from dispatcher where dispatcher_id="%s"' % dispatcher_id)).fetchall()
        if not exist:
            db.session.execute(
                text('insert dispatcher(dispatcher_id,dispatcher_name,dispatcher_phone) value("%s","%s","%s")' % (
                    dispatcher_id, dispatcher_name, dispatcher_phone)))
            db.session.commit()
            return jsonify(status=200, msg="添加成功")
        else:
            return jsonify(status=1000, msg="该编号已存在")
    if request.method == 'DELETE':
        want_delete = request.json.get('want_delete')
        db.session.execute(text('delete from dispatcher where dispatcher_id="%s"' % want_delete))
        db.session.commit()
        return jsonify(status=200, msg="解雇成功")


@app.route("/api/manager/wuliu", methods=["GET"])
@cross_origin()
def manager_wuliu():
    ended = request.args.get('id')
    if ended == '0':
        data = db.session.execute(text('select * from wuliu where ended=0')).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(order_id=data[i][0], cons_phone=data[i][1], disp_id=data[i][2], deliver_time=data[i][3])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)
    else:
        data = db.session.execute(text('select * from wuliu where ended=1')).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(order_id=data[i][0], cons_phone=data[i][1], disp_id=data[i][2], deliver_time=data[i][3])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)


@app.route("/api/manager/unsend", methods=["GET", "POST"])
@cross_origin()
def manager_unsend():
    if request.method == 'GET':
        data = db.session.execute(text('select * from oorder where checked=0')).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(order_id=data[i][0], shop_name=data[i][1], price=data[i][2], orderway=data[i][3],
                       cons_phone=data[i][4],
                       cons_name=data[i][5], cons_addre=data[i][6], create_time=data[i][8])
            Data.append(dic)

        disp_range = db.session.execute(text('select * from dispatcher')).fetchall()  # 获取所有的送货员就id，供选择
        Disp_range = []
        for i in range(len(disp_range)):
            dic = dict(disp_id=disp_range[i][0])
            Disp_range.append(dic)
        return jsonify(status=200, tabledata=Data, disp_range=Disp_range)
    if request.method == 'POST':
        rq = request.json
        order_id = rq.get('order_id')
        disp_id = rq.get('dispatcher_id')
        deliver_time = rq.get('deliver_time')
        cons_phone = db.session.execute(text('select cons_phone from oorder where order_id="%d"' % int(order_id))).first()

        db.session.execute(text('insert wuliu( order_id, cons_phone,disp_id,deliver_time) value(%d,"%s","%s","%s")' % (
        int(order_id), cons_phone[0], disp_id, deliver_time)))
        db.session.commit()
        return jsonify(status=200, msg="成功派发")


@app.route("/api/manager/sending", methods=["GET"])
@cross_origin()
def manager_sending():
    if request.method == 'GET':
        data = db.session.execute(text('select * from sending_order')).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(order_id=data[i][0], shop_name=data[i][1], order_money=data[i][2], order_way=data[i][3],
                       cons_phone=data[i][4],
                       cons_name=data[i][5], cons_addre=data[i][6], disp_id=data[i][7], deliver_time=data[i][8])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)


@app.route("/api/manager/sended", methods=["GET"])
@cross_origin()
def manager_sended():
    if request.method == 'GET':
        data = db.session.execute(text('select * from sended_order')).fetchall()
        Data = []
        for i in range(len(data)):
            dic = dict(order_id=data[i][0], shop_name=data[i][1], order_money=data[i][2], order_way=data[i][3],
                       cons_phone=data[i][4],
                       cons_name=data[i][5], cons_addre=data[i][6], disp_id=data[i][7], deliver_time=data[i][8])
            Data.append(dic)
        return jsonify(status=200, tabledata=Data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
