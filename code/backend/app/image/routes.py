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

photo_schema = PhotoSchema()

# Create boto3 client for AWS S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('S3_KEY'),
    aws_secret_access_key=os.getenv('S3_SECRET'),
    region_name=os.getenv('AWS_REGION')
)


@bp.route('/', methods=['GET'])
def get_photos():
    gallery_id = request.args.get('gallery_id')
    if not gallery_id:
        return jsonify({'error': 'Gallery ID is required'}), 400

    photos = Photo.query.filter_by(gallery_id=gallery_id).all()
    return jsonify(photo_schema.dump(photos, many=True))

@bp.route('/', methods=['POST'])
def upload_image():
    logging.debug(f"Incoming files: {request.files}")

    gallery_id = request.form.get('gallery_id')
    if not gallery_id:
        return jsonify({'error': 'Gallery ID is required'}), 400

    if 'files' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400

    uploaded_files = request.files.getlist('files')
    if not uploaded_files:
        return jsonify({'error': 'No selected files'}), 400

    uploaded_photos = []
    for file in uploaded_files:
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"

        try:
            s3_client.upload_fileobj(file, current_app.config['S3_BUCKET'], unique_filename)
        except Exception as e:
            logging.error(f"Error uploading file to S3: {e}")
            return jsonify({'error': 'Failed to upload file to S3'}), 500

        photo = Photo(filename=unique_filename, gallery_id=gallery_id)
        db.session.add(photo)
        uploaded_photos.append(photo)

    db.session.commit()

    return jsonify(photo_schema.dump(uploaded_photos, many=True)), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_photo(id):
    photo = Photo.query.get_or_404(id)

    try:
        s3_client.delete_object(Bucket=current_app.config['S3_BUCKET'], Key=photo.filename)
    except s3_client.exceptions.NoSuchKey:
        return jsonify({'error': 'Photo does not exist in the bucket'}), 404
    except Exception as e:
        logging.error(f"Error deleting file from S3: {e}")
        return jsonify({'error': 'Failed to delete file from S3'}), 500

    db.session.delete(photo)
    db.session.commit()

    return jsonify({'message': 'Photo deleted successfully'}), 200

from flask import jsonify

@bp.route('/test-s3-connection', methods=['GET'])
def test_s3_connection():
    try:
        # Debug-Informationen sammeln
        bucket = current_app.config['S3_BUCKET']
        credentials = {
            'region': os.getenv('AWS_REGION'),
            'key_exists': bool(os.getenv('S3_KEY')),
            'secret_exists': bool(os.getenv('S3_SECRET')),
            'bucket': bucket
        }
        
        # S3 Test durchführen
        response = s3_client.list_objects_v2(
            Bucket=bucket,
            MaxKeys=1
        )
        
        return jsonify({
            'status': 'success',
            'message': 'S3 Verbindung erfolgreich',
            'credentials_check': credentials,
            'response': {
                'bucket': response.get('Name'),
                'prefix': response.get('Prefix'),
                'max_keys': response.get('MaxKeys')
            }
        }), 200
        
    except Exception as e:
        logging.error(f"S3 Verbindungsfehler: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'S3 Verbindung fehlgeschlagen',
            'error_details': str(e),
            'credentials_check': credentials
        }), 500