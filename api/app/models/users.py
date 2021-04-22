from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from ..extensions import db

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
