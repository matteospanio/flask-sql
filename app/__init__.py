from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret string'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://matteo:password@localhost/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_RECORD_QUERIES'] = True
    app.config['SESSION_PERMANENT'] = False

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth,  url_prefix='/auth')

    return app
