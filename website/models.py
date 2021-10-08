# database models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cuisines = db.relationship('Cuisines')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    nickname = db.Column(db.String(150))
    recipe = db.relationship('Recipe')


class Cuisines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(1000))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
