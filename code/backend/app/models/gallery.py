from app.extensions import db

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    cover_image_url = db.Column(db.String(256), nullable=True)
    photos = db.relationship('Photo', backref='gallery', lazy=True)