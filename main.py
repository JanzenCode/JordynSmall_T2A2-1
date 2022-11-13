from flask import Flask
from init import db, ma, bcrypt, jwt
from controllers.Command_Controller import db_commands
from controllers.Auth_Controller import auth_bp
from controllers.User_Controller import user_bp
from controllers.Products_Controller import products_bp
from controllers.AddressController import address_bp
from controllers.Order_Controller import orders_bp
from marshmallow.exceptions import ValidationError
import os 

def create_app():
    app = Flask(__name__)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400

    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400

    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': 'You are not authorized to perform this action'}, 401

    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400

    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(db_commands)
    app.register_blueprint(user_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(orders_bp)

    return app
