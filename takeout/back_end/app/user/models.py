from flask_sqlalchemy import SQLAlchemy

# 创建数据库对象
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    sex = db.Column(db.String(5), nullable=False)
    role = db.Column(db.String(5), nullable=False)
    username = db.Column(db.String(20), primary_key=True)
    realname = db.Column(db.String(20), nullable=False)
    telephone = db.Column(db.BigInteger, primary_key=True)
    password = db.Column(db.String(12), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
