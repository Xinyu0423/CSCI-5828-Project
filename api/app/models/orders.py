from flask_sqlalchemy import SQLAlchemy
from ..extensions import db
from .products import Products 

class Orders(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    o_uid=db.Column(db.Integer,db.ForeignKey('users.uid'),nullable=False) 
    o_pid=db.Column(db.Integer,db.ForeignKey('products.pid')) #order product id, could be multiple
    otime=db.Column(db.DateTime,nullable=False)  #order date
    address=db.Column(db.String(255), nullable=True) 
    quantity=db.Column(db.Integer, nullable=True)
    item=db.Column(db.String(255), nullable=True) 
    pid = db.relationship('Products')
