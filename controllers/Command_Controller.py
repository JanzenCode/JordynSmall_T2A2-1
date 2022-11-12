from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.users import User
from models.products import Products
from models.address import Address

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
            email='vintagedev@spam.com',
            password=bcrypt.generate_password_hash('123').decode('utf-8'),
            first_name='Adam',
            last_name='User',
            is_admin=True
        ),
        User(
            first_name='Ron',
            last_name='Swanson',
            email='swanson@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
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
        )
    ]
    db.session.add_all(products)
    db.session.commit()
    print('Tables Seeded')