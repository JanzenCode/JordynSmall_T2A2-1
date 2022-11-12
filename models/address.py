from init import db, ma 
from marshmallow import fields 
from models.users import User

class Address(db.Model):
    __tablename__ = 'address'

    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    id = db.Column(db.Integer(), nullable=False, foreign_key=("Users.id"))

class AddressSchema(ma.Schema):
    class Meta:
        fields = ('address', 'city', 'state', 'country', 'id')