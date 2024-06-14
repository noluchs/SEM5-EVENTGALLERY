from apiflask import APIFlask, Schema, APIBlueprint
from flask import request, jsonify, current_app
from .models import Gallery, Photo
from .schemas import GallerySchema, PhotoSchema
from .extensions import db, get_s3_client, get_rekognition_client
from marshmallow import ValidationError, fields  # Ensure fields is imported from marshmallow

app = APIFlask(__name__, title="APIFlask", version="0.1.0")

class HTTPErrorSchema(Schema):
    message = fields.Str()

gallery_bp = APIBlueprint('gallery', __name__)
image_bp = APIBlueprint('image', __name__)


@gallery_bp.route('/api/gallery', methods=['GET'])
@app.output(GallerySchema(many=True))
def get_galleries():
    galleries = Gallery.query.all()
    return galleries

@gallery_bp.route('/api/gallery', methods=['POST'])
@app.input(GallerySchema, location='json')
@app.output(GallerySchema, status_code=201)
def create_gallery(data):
    gallery = Gallery(name=data['name'])
    db.session.add(gallery)
    db.session.commit()
    return gallery

@gallery_bp.route('/api/gallery/<int:id>', methods=['DELETE'])
@app.output({}, status_code=204)
@app.doc(responses={404: "Not found"})
def delete_gallery(id):
    gallery = Gallery.query.get_or_404(id)
    db.session.delete(gallery)
    db.session.commit()
    return '', 204

@image_bp.route('/api/image', methods=['POST'])
@app.input(PhotoSchema, location='files')
@app.output(PhotoSchema, status_code=201)
def upload_image(data):
    file = request.files['file']
    s3_client = get_s3_client()
    filename = file.filename
    s3_client.upload_fileobj(file, current_app.config['S3_BUCKET'], filename)

    photo = Photo(filename=filename, gallery_id=data['gallery_id'])
    db.session.add(photo)
    db.session.commit()
    return photo

@image_bp.route('/api/image/filter', methods=['POST'])
@app.input(PhotoSchema, location='files')
@app.output(PhotoSchema(many=True))
def filter_images(data):
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


app.register_blueprint(gallery_bp)
app.register_blueprint(image_bp)