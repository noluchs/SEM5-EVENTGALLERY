import jwt
from datetime import datetime, timedelta
from flask import current_app

def generate_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
