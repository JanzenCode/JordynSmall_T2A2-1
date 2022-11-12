from flask import Blueprint, request
from init import db, ma, bcrypt, jwt
from sqlalchemy.exc import IntegrityError
from models.address import Address, AddressSchema
from models.users import User

address_bp = Blueprint('address',__name__, url_prefix='/auth')

@address_bp.route('/register/address ')
def auth_register():
    try:
        user_address = Address(
            address = request.json('address'),
            city = request.json('city'),
            state = request.json('state'),
            country = request.json('country'),
            id = request.json('User.id')
        )
        db.session.add(user_address)
        db.session.commit()
        return AddressSchema(exclude = ['password']).dump(user_address), 201
    except IntegrityError:
        return {'error': 'this user already has an address, use a patch to update the users details'}, 409