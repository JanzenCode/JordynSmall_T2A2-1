from init import db, ma 
from marshmallow import fields 

class products(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    brand = db.Column(db.String, nullable=False)
    style = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class ProductSchema(ma.Schema):
    class Meta:
        fields = 
