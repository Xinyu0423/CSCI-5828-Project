from flask_sqlalchemy import SQLAlchemy

from ..extensions import db

class Products(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    rating=db.Column(db.Float)  #product rating
    price=db.Column(db.Float)
    intro=db.Column(db.String(256))
    