from init import db, ma 
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_CATEGORY = ['Shirts', 'Sweaters', 'Hoodies', 'Pants', 'Shoes', 'Accessories', 'Jewellery']
VALID_BRAND = ['Nike', 'Addidas', ' Under Armour', ' Lululemon', "Levi's", 'Von Dutch', 'Diesel', 'Tommy Hilfiger', 'Nautica', 'Ralph Lauren', 'Wrangler', 'Target', 'Anko', 'Prada', 'Chanel', 'Other Brands', 'No Brand']

class products(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String)
    brand = db.Column(db.String, nullable=False)
    style = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class ProductSchema(ma.Schema):
    description = fields.String()
    category = fields.String(required=True, validate=OneOf(VALID_CATEGORY))
    brand = fields.String(required=True, validate=OneOf(VALID_BRAND))
    class Meta:
        fields = ('product_id', 'description', 'brand', 'style', 'category', 'size', 'price', 'quantity')
        ordered = True 
