from datetime import datetime
from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    photos = db.relationship('Photo', backref='user', lazy=True)
    face_recognitions = db.relationship('FaceRecognition', backref='user', lazy=True)
