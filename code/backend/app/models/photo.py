from app.extensions import db
from datetime import datetime

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallery.id'), nullable=False)