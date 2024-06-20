from app.gallery import bp
from flask import Blueprint, request, jsonify, current_app
from app.models import Gallery
from app.schemas import GallerySchema
from app.extensions import db
import logging

@bp.route('/', methods=['GET'])
def get_galleries():
    galleries = Gallery.query.all()
    return jsonify([gallery.to_dict() for gallery in galleries])

@bp.route('/', methods=['POST'])
def create_gallery():
    data = request.get_json()
    logging.debug(f"Incoming request data: {data}")

    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    gallery = Gallery(name=name)
    db.session.add(gallery)
    db.session.commit()

    return jsonify(gallery.to_dict()), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_gallery(id):
    gallery = Gallery.query.get_or_404(id)
    db.session.delete(gallery)
    db.session.commit()

    return jsonify({'message': 'Gallery deleted successfully'}), 200