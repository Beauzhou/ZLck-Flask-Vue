from functools import wraps
from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def login_required(view_func):
    @wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            # get token from request header
            token = request.headers["Authorization"]
        except Exception:
            # thrown error if token is not exist
            return jsonify(msg='token is not exist'), 402
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return jsonify(msg="Login expired"), 401
        return view_func(*args, **kwargs)

    return verify_token


def token_info():
    token = request.headers["Authorization"]
    s = Serializer(current_app.config["SECRET_KEY"])
    return s.loads(token)
