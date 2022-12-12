import traceback
from app.user.model import User
from app.exts import db
from flask import request, jsonify
from app.auto.create_token import generate_token
from app.configUtils import ConfigUtils
from app.util.Jsonify import Jsonify
from ..user import user
import redis

# return 500 error
from ..util.pymysql import mysql

conf = ConfigUtils()
cf = conf.get_config()


@user.errorhandler(500)
def handler_exception(e):
    response = dict(message=traceback.format_exc())
    return jsonify(response), 500


# 查询
@user.route("/search", methods=['GET'])
def search():
    obj = User.query.all()
    list = []
    for i in obj:
        list.append(i.to_json_all())
    return Jsonify.query_all(list)


# 查询
@user.route("/search/<id>", methods=['GET'])
def searchId(id):
    sql = "select * from user where id = %s"
    # obj = User.query.filter_by(id=id).first()
    # # obj.to_json()
    # obj1 = obj.to_json()

    return Jsonify.success(mysql.get_one(sql, id))


# 注册
@user.route('/register', methods=['POST'])
def register():
    # try:
    js = request.get_json()
    email = js.get('email')
    _password = js.get('password')
    username = js.get('username')
    is_staff = js.get("is_staff")
    email_validation = js.get("verificationEmail")
    pool = redis.ConnectionPool(host=cf.get("redis", "REDIS_HOST"), port=6379, db=0, decode_responses=True)
    red = redis.StrictRedis(connection_pool=pool)
    email_validation1 = red.get(email)
    if email_validation != str(email_validation1):
        return jsonify({"msg": "验证码错误或者过期,请重新发送"}), 801
    if is_staff is None:
        is_staff = 0
    obj = User.query.filter_by(email=email).first()
    if obj is None:
        save = User(username=username, email=email, _password=_password, is_staff=is_staff)
        save.hash_password(_password)
        # 上传提交插入的字段
        db.session.add(save)
        db.session.commit()
        # 此处设定请求后的返回值：
        return jsonify({"code": "200", "msg": "注册成功"})
    else:
        return jsonify({"msg": "邮箱：" + email + "已存在"}), 801


@user.route('/login', methods=['POST'])
def login():
    js = request.get_json()
    email = js.get('email')
    _password = js.get('password')
    obj = User.query.filter_by(email=email).first()
    if not obj:
        return jsonify({"msg": "邮箱不存在"}), 802
    if obj.verify_password(_password):
        token = generate_token(email, obj.role_id)
        info = obj.to_json()
        return jsonify({"code": "200", "msg": "登录成功", "token": token, "userInfo": info,
                        "roleId": info['roleId']})
    else:
        return jsonify({"msg": "密码错误"}), 803


# 修改
@user.route("/update", methods=['PUT'])
def update():
    sql = "update user set signature = %s, avatar = %s where id = %s"
    js = request.get_json()
    id1 = js.get('id')
    signature = js.get('signature')
    avatar = js.get('avatar')
    # obj = User.query.filter_by(id=id1).first()
    # obj.signature = signature
    # obj.avatar = avatar
    # db.session.commit()
    mysql.modify(sql, (signature, avatar, id1))
    return Jsonify.update()


# 删除
@user.route("/delete/<id>", methods=['DELETE'])
def delete(id):
    sql = "delete from post where author_id = %s"
    sql1 = "delete from comment where author_id = %s"
    mysql.delete(sql, id)
    mysql.delete(sql1, id)
    user_delete = User.query.filter_by(id=id).first()
    db.session.delete(user_delete)
    db.session.commit()
    return Jsonify.delete()
