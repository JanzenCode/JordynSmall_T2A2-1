from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.users import User
from models.products import Products
from models.address import Address
from models.orders import Order

db_commands = Blueprint('db', __name__)

#General Commands for Database Management and Testing
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email='vintagestockhand@spam.com',
            password=bcrypt.generate_password_hash('123').decode('utf-8'),
            first_name='Adam',
            last_name='User',
            is_admin=True,
            street_number = '69',
            street_name = 'Vintage Way',
            suburb = 'Recycler',
            postcode = '4101'
        ),
        User(
            first_name='Ron',
            last_name='Swanson',
            email='swanson@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8'),
            street_number = '1',
            street_name = 'Swanson Rd',
            suburb = 'Pawee',
            postcode = '5011'
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    addresses = [
        Address(
            street_number = '69',
            street_name = 'Vintage Way',
            suburb = 'Recycler',
            postcode = '4101',
            user = users[0]
        ),

        Address(
            street_number = '1',
            street_name = 'Swanson Rd',
            suburb = 'Pawee',
            postcode = '5011',
            user = users[1]
        )
    ]
    db.session.add_all(addresses)
    db.session.commit()

    products = [
        Products(
            description = 'Black Heavy Hoodie',
            brand = 'Nike',
            style = 'Street Style',
            category = 'Hoodies',
            size = 'Large',
            price = '99',
            quantity = '1'
        ),
        Products(
            description = 'White T-Shirt',
            brand = 'Nautica',
            style = 'Beach Style',
            category = 'Shirts',
            size = 'Medium',
            price = '50',
            quantity = '1'
        ),
        Products(
            description = 'Canvas Tote Bag',
            brand = 'No Brand',
            style = 'Casual Wear',
            category = 'Accessories',
            size = 'XL',
            price = '20',
            quantity = '1'
        ),
        Products(
            description = 'Air Force One',
            brand = 'Nike',
            style = 'Street Wear',
            category = 'Shoes',
            size = 'EU44',
            price = '110',
            quantity = '1'
        ),
        Products(
            description = 'Sterling Silver Rings',
            brand = 'No Brand',
            style = 'Causal Wear',
            category = 'Jewellery',
            size = 'RS9',
            price = '30',
            quantity = '3'
        )
    ]
    db.session.add_all(products)
    db.session.commit()
    
    orders = [
        Order(
        quantity = '1',
        subtotal = '99',
        user_id = users[1]
    )
    ]
    db.session.add_all(orders)
    db.session.commit()

    print('Tables Seeded')