from flask import Blueprint, request, jsonify
from app.image.models import Photo
from app.extensions import db
import os
import uuid


image_bp = Blueprint('image', __name__)

@image_bp.route('/', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    return jsonify([photo.to_dict() for photo in photos])

@image_bp.route('/', methods=['POST'])
@app.input(PhotoSchema, location='files')
@app.output(PhotoSchema, status_code=201)
def upload_image(data):
    file = request.files['file']
    s3_client = get_s3_client()

    # Split the filename into name and extension
    filename, file_extension = os.path.splitext(file.filename)

    # Generate a random name for the image
    random_name = f"{filename}_{uuid.uuid4()}{file_extension}"

    s3_client.upload_fileobj(file, current_app.config['S3_BUCKET'], random_name)

    photo = Photo(filename=random_name, gallery_id=data['gallery_id'])
    db.session.add(photo)
    db.session.commit()
    return photo


@image_bp.route('/<int:id>', methods=['DELETE'])
def delete_photo(id):
    photo = Photo.query.get_or_404(id)
    s3_client = get_s3_client()

    try:
        s3_client.delete_object(Bucket=current_app.config['S3_BUCKET'], Key=photo.filename)
    except ClientError as e:
        # If the object does not exist in the bucket, return an error message
        if e.response['Error']['Code'] == 'NoSuchKey':
            return jsonify({'error': 'Photo does not exist in the bucket'}), 404
        else:
            raise

    db.session.delete(photo)
    db.session.commit()

    return jsonify({'message': 'Photo deleted successfully'}), 200