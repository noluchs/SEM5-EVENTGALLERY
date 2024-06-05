from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.models import User
from app.extensions import db
from app.auth.auth_utils import generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password_hash=hashed_password, name=request.json['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(email=request.json['email']).first()
    if user and check_password_hash(user.password_hash, request.json['password']):
        token = generate_token(user.id)
        return jsonify({"token": token})
    else:
        return jsonify({"message": "Invalid credentials"}), 401
