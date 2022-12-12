from flask import Flask
from app.exts import db

app = Flask(__name__)

from app import config


def create_app():
    app.config.from_object(config)
    db.app = app
    db.init_app(app=app)
    # # blueprint
    from app.user import user
    from app.post import post
    from app.comment import detail
    from app.file import file
    from app.banner import banner
    from app.email import email
    db.create_all()
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(post, url_prefix='/post')
    app.register_blueprint(detail, url_prefix='/detail')
    app.register_blueprint(file, url_prefix='/file')
    app.register_blueprint(banner, url_prefix='/banner')
    app.register_blueprint(email, url_prefix='/email')
    return app
