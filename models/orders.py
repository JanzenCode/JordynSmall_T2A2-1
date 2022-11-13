# from init import db, ma 
# from marshmallow import fields

# class Order(db.Model):
#     __tablename__ = 'Orders'

#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)

#     user = db.relationship('User', back_populates='order_placed')

# class OrderSchema(ma.Schema):
#     user = fields.Nested('UserSchema', only=['first_name', 'last_name', 'email'])

#     class Meta:
#         fields = ('id', 'date', 'quantity', 'user_id')
#         ordered = True
