from . import db

class User(db.Model):
    __tablename__ = 'user'

    sex       = db.Column(db.String(5), nullable=False)
    role      = db.Column(db.String(5), nullable=False)
    username  = db.Column(db.String(20), primary_key=True)
    realname  = db.Column(db.String(20), nullable=False)
    telephone = db.Column(db.BigInteger, primary_key=True)
    password  = db.Column(db.String(12), nullable=False)

    def __init__(self, username, password, telephone, role):
        """ 初始化用户信息 """
        self.sex       = ""
        self.role      = role
        self.username  = username
        self.realname  = ""
        self.telephone = telephone
        self.password  = password

    def __repr__(self):
        return f'<User {self.username}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

class Shop(db.Model):
    __tablename__ = 'shop'

    name    = db.Column(db.String(255), primary_key=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __init__(self, ):
        """ 初始化商店信息 """
        self.shopID  = 0
        self.name    = ""
        self.address = ""

    def __repr__(self):
        return f'<User {self.username}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

class Food(db.Model):
    __tablename__ = 'food'

    shopName = db.Column(db.Integer, nullable=False)
    name     = db.Column(db.String(255), primary_key=True, nullable=False)
    price    = db.Column(db.Float, nullable=False)
    image    = db.Column(db.String(255), nullable=False)

    def __init__(self, ):
        """ 初始化食品信息 """
        self.name    = ""
        self.price   = 0.0
        self.img     = ""

    def __repr__(self):
        return f'<User {self.username}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

class Order(db.Model):
    __tablename__ = 'order'

    username = db.Column(db.String(255), primary_key = True, nullable=False)
    foodName = db.Column(db.String(255), nullable=False)
    orderPrice = db.Column(db.Float, nullable=False)
    orderWay = db.Column(db.String(255), nullable=False)
    consName = db.Column(db.String(255), nullable=False)
    consPhone = db.Column(db.BigInteger, nullable=False)
    consAddress = db.Column(db.String(255), nullable=False)

    def __init__(self):
        """ 初始化订单信息 """
        self.username = ""
        self.foodName = ""
        self.orderPrice = 0.0
        self.orderWay = ""
        self.consName = ""
        self.consPhone = 0
        self.consAddress = ""

    def __init__(self, username, foodName, orderPrice, orderWay, consName, consPhone, consAddress):
        """ 初始化订单信息 """
        self.username = username
        self.foodName = foodName
        self.orderPrice = orderPrice
        self.orderWay = orderWay
        self.consName = consName
        self.consPhone = consPhone
        self.consAddress = consAddress

    def __repr__(self):
        return f'<User {self.username}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
