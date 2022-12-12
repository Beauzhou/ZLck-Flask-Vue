import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app.exts import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(200), nullable=False)
    avatar = db.Column(db.String(100), nullable=True)
    signature = db.Column(db.String(100), nullable=True)
    join_time = db.Column(db.DateTime, default=datetime.datetime.now())
    is_staff = db.Column(db.Integer)
    is_active = db.Column(db.Integer)
    role_id = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "roleId": self.role_id,
            "username": self.username,
            "avatar": self.avatar,
            "is_staff": self.is_staff,
            "email": self.email,
            "signature": self.signature
        }

    def to_json_all(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "join_time": self.join_time,
            "is_staff": self.is_staff,
            "is_active": self.is_active,
            "signature": self.signature
        }

    def __init__(self, username, _password, email, is_staff):
        self.username = username
        self._password = _password
        self.email = email
        self.is_staff = is_staff

    def hash_password(self, _password):  # 密码加密方法
        self._password = generate_password_hash(_password)

    def verify_password(self, _password):  # 验证密码方法
        return check_password_hash(self._password, _password)
