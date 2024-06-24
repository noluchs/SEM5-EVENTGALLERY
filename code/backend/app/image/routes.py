from app.image import bp
from flask import Blueprint, request, jsonify, current_app
from app.models import Photo
from app.schemas import PhotoSchema
from app.extensions import db
from werkzeug.utils import secure_filename
import os
import uuid
import boto3
import logging


# Create boto3 client for AWS S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
)


@bp.route('/', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    return jsonify([photo.to_dict() for photo in photos])


@bp.route('/', methods=['POST'])
@bp.input(PhotoSchema, location='files')
@bp.output(PhotoSchema, status_code=201)
def upload_image(data):
    logging.debug(f"Incoming request data: {data}")
    logging.debug(f"Incoming files: {request.files}")

    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    unique_filename = f"{filename}_{uuid.uuid4().hex}"

    try:
        s3.upload_fileobj(file, current_app.config['S3_BUCKET'], unique_filename)
    except Exception as e:
        logging.error(f"Error uploading file to S3: {e}")
        return jsonify({'error': 'Failed to upload file to S3'}), 500

    photo = Photo(filename=unique_filename, gallery_id=data['gallery_id'])
    db.session.add(photo)
    db.session.commit()

    return photo


@bp.route('/<int:id>', methods=['DELETE'])
def delete_photo(id):
    photo = Photo.query.get_or_404(id)
    s3_client = get_s3_client()

    try:
        s3_client.delete_object(Bucket=current_app.config['S3_BUCKET'], Key=photo.filename)
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return jsonify({'error': 'Photo does not exist in the bucket'}), 404
        else:
            raise

    db.session.delete(photo)
    db.session.commit()

    return jsonify({'message': 'Photo deleted successfully'}), 200