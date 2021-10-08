from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'SQLITE:///{DB_NAME}'

    db.init_app(app)

    # Routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
