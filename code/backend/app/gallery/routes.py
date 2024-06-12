from flask import request, jsonify, Blueprint
from app.extensions import db
from app.gallery.models import Gallery
from app.schemas import GallerySchema

gallery_bp = Blueprint('gallery', __name__)
gallery_schema = GallerySchema()
galleries_schema = GallerySchema(many=True)

@gallery_bp.route('/galleries', methods=['POST'])
def create_gallery():
    data = request.json
    gallery = gallery_schema.load(data)
    db.session.add(gallery)
    db.session.commit()
    return gallery_schema.jsonify(gallery), 201

@gallery_bp.route('/galleries', methods=['GET'])
def get_galleries():
    galleries = Gallery.query.all()
    return galleries_schema.jsonify(galleries), 200