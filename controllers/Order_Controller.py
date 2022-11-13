from flask import Blueprint, request, abort
from init import db
from datetime import date
from models.products import Products, ProductSchema
from models.orders import Order, OrderSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('/new_order', methods=['POST'])
@jwt_required
def new_order():
    data = ProductSchema().load(request.json)
    order = Order(
        date = date.today(),
        user_id = get_jwt_identity(),
        product_id = request.json('product_id'),
    )
    db.session.add
    db.session.commit()


    