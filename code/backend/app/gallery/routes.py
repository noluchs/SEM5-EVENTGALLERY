from flask import Blueprint, request, jsonify
from app.gallery.models import Gallery
from app.extensions import db

gallery_bp = Blueprint('gallery', __name__)

@gallery_bp.route('/', methods=['GET'])
def get_galleries():
    galleries = Gallery.query.all()
    return jsonify([gallery.to_dict() for gallery in galleries])

@gallery_bp.route('/', methods=['POST'])
def create_gallery():
    name = request.json['name']
    event_id = request.json['event_id']
    new_gallery = Gallery(name=name, event_id=event_id)
    db.session.add(new_gallery)
    db.session.commit()
    return jsonify(new_gallery.to_dict()), 201
