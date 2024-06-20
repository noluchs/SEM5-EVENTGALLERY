from apiflask import APIFlask, Schema, APIBlueprint, HTTPError
from flask import request, jsonify, current_app
from flask_cors import CORS
from .models import Photo, Gallery
from .schemas import PhotoSchema, GallerySchema
from .extensions import db, get_s3_client, get_rekognition_client
from marshmallow import ValidationError, fields

app = APIFlask(__name__, title="APIFlask", version="0.1.0")

# Enable CORS for all routes under /api/*
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

class HTTPErrorSchema(Schema):
    message = fields.Str()

gallery_bp = APIBlueprint('gallery', __name__)
image_bp = APIBlueprint('image', __name__)

@gallery_bp.route('/gallery', methods=['GET'])
@app.output(GallerySchema(many=True))
def get_galleries():
    galleries = Gallery.query.all()
    return galleries

@gallery_bp.route('/gallery', methods=['POST'])
@app.input(GallerySchema, location='json')
@app.output(GallerySchema, status_code=201)
def create_gallery(json_data):
    try:
        gallery = Gallery(name=json_data['name'])
        db.session.add(gallery)
        db.session.commit()
        return gallery
    except Exception as e:
        app.logger.error(f"Error creating gallery: {e}")
        raise HTTPError(500, "Internal server error", details=str(e))

@gallery_bp.route('/gallery/<int:id>', methods=['DELETE'])
@app.output({}, status_code=204)
@app.doc(responses={404: "Not found"})
def delete_gallery(id):
    try:
        gallery = Gallery.query.get_or_404(id)
        db.session.delete(gallery)
        db.session.commit()
        return '', 204
    except Exception as e:
        app.logger.error(f"Error deleting gallery with id {id}: {e}")
        raise HTTPError(500, "Internal server error", details=str(e))

@image_bp.route('/image', methods=['POST'])
@app.input(PhotoSchema, location='files')
@app.output(PhotoSchema, status_code=201)
def upload_image(data):
    try:
        file = request.files['file']
        s3_client = get_s3_client()
        filename = file.filename
        s3_client.upload_fileobj(file, current_app.config['S3_BUCKET'], filename)

        photo = Photo(filename=filename, gallery_id=data['gallery_id'])
        db.session.add(photo)
        db.session.commit()
        return photo
    except Exception as e:
        app.logger.error(f"Error uploading image: {e}")
        raise HTTPError(500, "Internal server error", details=str(e))

@image_bp.route('/image/filter', methods=['POST'])
@app.input(PhotoSchema, location='files')
@app.output(PhotoSchema(many=True))
def filter_images(data):
    try:
        rekognition_client = get_rekognition_client()
        image = request.files['file']
        response = rekognition_client.search_faces_by_image(
            CollectionId='YourCollectionId',
            Image={'Bytes': image.read()},
            MaxFaces=5,
            FaceMatchThreshold=90
        )

        face_ids = [match['Face']['FaceId'] for match in response['FaceMatches']]
        photos = Photo.query.filter(Photo.face_id.in_(face_ids)).all()
        return photos
    except Exception as e:
        app.logger.error(f"Error filtering images: {e}")
        raise HTTPError(500, "Internal server error", details=str(e))

app.register_blueprint(gallery_bp, url_prefix='/api')
app.register_blueprint(image_bp, url_prefix='/api')
