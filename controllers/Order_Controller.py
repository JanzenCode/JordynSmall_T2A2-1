# from flask import Blueprint, request
# from init import db
# from datetime import date
# from models.products import Products, ProductSchema
# from models.orders import Order, OrderSchema
# from flask_jwt_extended import jwt_required, get_jwt_identity

# orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

# @orders_bp.route('/new_order/', methods=['POST'])
# @jwt_required
# def new_order():
#     orders = Order(
#         date = date.today(),
#         user_id = get_jwt_identity(),
#     )
#     db.session.add(orders)
#     db.session.commit()

#     order_placed = Order(
#         order_id = orders.id, 
#         product_id = request.json.get('product_id'),
#         quantity = request.json.get('quantity'),
#     )
#     db.session.add(order_placed)
#     db.session.commit()




    