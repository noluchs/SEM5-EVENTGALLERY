from app.extensions import db

class Gallery(db.Model):
    __tablename__ = 'galleries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    photos = db.relationship('Photo', back_populates='gallery')