from flask import request, jsonify, Blueprint
from app.extensions import db
from app.gallery.models import Gallery
from app.schemas import GallerySchema

gallery_bp = Blueprint('gallery', __name__)
gallery_schema = GallerySchema()
galleries_schema = GallerySchema(many=True)

# Corrected code to align with the provided models
@gallery_bp.route('/create', methods=['POST'])
def create_gallery():
    data = request.get_json()
    new_gallery = Gallery(
        title=data.get('title'),  # Corrected field name
        description=data.get('description'),
        user_id=data.get('user_id')
    )
    db.session.add(new_gallery)
    db.session.commit()
    return jsonify({"message": "Gallery created"}), 201

@gallery_bp.route('/galleries', methods=['GET'])
def get_galleries():
    galleries = Gallery.query.all()
    return galleries_schema.jsonify(galleries), 200