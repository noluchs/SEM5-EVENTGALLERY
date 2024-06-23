from apiflask import Schema
from apiflask.fields import String, Integer, Boolean
from apiflask.validators import Length, Email
from flask import current_app
from jwt import encode as jwt_encode, decode as jwt_decode
from jwt import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

# define the user table
class UsersModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean)

    def __init__(self, email, name, password, is_admin=False):
        self.email = email
        self.name = name
        self.is_admin = is_admin
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expires_in=600):
        exp_timestamp = int(datetime.now(timezone.utc).timestamp()) + expires_in
        return jwt_encode(
            {'id': self.id, 'exp': exp_timestamp},
            current_app.config['SECRET_KEY'], algorithm='HS256'
        )

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt_decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            return UsersModel.query.filter_by(id=data['id']).first()
        except ExpiredSignatureError:
            return None
        except InvalidTokenError:
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def get_roles(user):
        user_role = ["User"]
        if user.is_admin:
            user_role = ["Admin"]
        return user_role

# define the schema for the user input
class UsersIn(Schema):
    name = String(required=True, validate=Length(0, 128))
    email = String(required=True, validate=[Length(0, 128), Email()])
    password = String(required=True, validate=Length(0, 128))
    is_admin = Boolean(required=False, load_default=False)

# define the schema for the output
class UsersOut(Schema):
    id = Integer()
    name = String()
    email = String()
    is_admin = Boolean()
    password = String()

class LoginIn(Schema):
    email = String(required=True, validate=[Length(0, 128), Email()])
    password = String(required=True, validate=Length(0, 128))

class TokenOut(Schema):
    token = String()
    duration = Integer()