from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def generate_token(user, user_id):
    expiration = 36000
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)  # expiration
    token = s.dumps({'user': user, 'userId': user_id}).decode('ascii')
    return token
