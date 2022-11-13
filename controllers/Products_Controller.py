from flask import Blueprint, request
from init import db
from models.products import Products, ProductSchema
from flask_jwt_extended import jwt_required

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/new_product/', methods=['POST'])
@jwt_required()
def add_product():
    product = Products(
        description = request.json.get('description'),
        brand = request.json.get('brand'),
        style = request.json.get('style'),
        category = request.json.get('category'),
        size = request.json.get('size'),
        price = request.json.get('price'),
        quantity = request.json.get('quantity')
    )

    db.session.add(product)
    db.session.commit()
    return ProductSchema().dump(product)

# View all available products
@products_bp.route('/', methods=['GET'])
@jwt_required()
def get_products():
    stmt = db.select(Products)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# Sort by Category
@products_bp.route('/<string:category>/', methods=['GET'])
@jwt_required()
def filter_by_category(category):
    stmt = db.select(Products).filter_by(category=category)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# Sort by Brand
@products_bp.route('/<string:brand>/', methods=['GET'])
@jwt_required()
def filter_by_brand(brand):
    stmt  = db.select(Products).filter_by(brand=brand)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# Sort by Style
@products_bp.route('/<string:style>/', methods=['GET'])
@jwt_required()
def filter_by_style(style):
    stmt = db.select(Products).filter_by(style=style)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# Sort by Price 
@products_bp.route('/<int:price>/')
@jwt_required()
def filter_by_price(price):
    stmt = db.select(Products).filter_by(price=price)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)



