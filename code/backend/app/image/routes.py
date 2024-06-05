from flask import Blueprint, request, jsonify
from app.image.models import Photo
from app.extensions import db

image_bp = Blueprint('image', __name__)

@image_bp.route('/', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    return jsonify([photo.to_dict() for photo in photos])

@image_bp.route('/', methods=['POST'])
def upload_photo():
    url = request.json['url']
    user_id = request.json['user_id']
    gallery_id = request.json['gallery_id']
    new_photo = Photo(url=url, user_id=user_id, gallery_id=gallery_id)
    db.session.add(new_photo)
    db.session.commit()
    return jsonify(new_photo.to_dict()), 201
