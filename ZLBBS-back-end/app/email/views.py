import traceback
from app.util.Jsonify import Jsonify
from flask import jsonify
from ..email import email

from app import app
from flask_mail import Mail, Message
from app.configUtils import ConfigUtils
from app.util.random import rand

import pickle as pk
import redis

conf = ConfigUtils()
cf = conf.get_config()

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = cf.get("email", "email")
app.config['MAIL_PASSWORD'] = cf.get("email", "password")
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

pool = redis.ConnectionPool(host=cf.get("redis", "REDIS_HOST"), port=6379, db=0, decode_responses=True)
red = redis.StrictRedis(connection_pool=pool)


# return 500 error
@email.errorhandler(500)
def handler_exception(e):
    response = dict(message=traceback.format_exc())
    return jsonify(response), 500


@email.route("/send/<e_mail>", methods=['POST'])
def send(e_mail):
    msg = Message("知了传课Python论坛--邮箱验证码", sender=cf.get("email", "email"), recipients=[e_mail])
    validation = rand()
    msg.body = "你好， 你的验证码为" + validation + ", 验证码5分钟内有效"
    try:
        red.set(e_mail, validation)
        red.expire(e_mail, 300)
        mail.send(msg)
        return Jsonify.success("验证码已发送，请查收邮件")
    except:
        return Jsonify.error("系统错误，请联系管理员")
