from .extensions import db

class Gallery(db.Model):
    __tablename__ = 'galleries'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

    event = db.relationship('Event', back_populates='galleries')
    photos = db.relationship('Photo', back_populates='gallery')