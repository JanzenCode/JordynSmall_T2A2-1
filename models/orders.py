from init import db, ma 
from marshmallow import fields

class Order(db.Model):
    __tablename__ = 'Orders'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date_placed = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

user = db.relationship('User')
order_placed = db.relationship('Product', back_populates='product', cascade='all, delete')

class OrderSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['first_name', 'last_name', 'email'])

    class Meta:
        fields = ('id', 'date_placed', 'quantity','subtotal', 'user_id')
        ordered = True
