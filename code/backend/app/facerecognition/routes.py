# app/facerecognition/routes.py

from app.facerecognition import bp
from flask import Blueprint, request, jsonify, current_app
from app.models import Photo
from app.extensions import db
import boto3
import base64
import os
from boto3.session import Session

# Load environment variables
aws_access_key = os.getenv('AWS_REKOGNITION_KEY')
aws_secret_key = os.getenv('AWS_REKOGNITION_SECRET')
aws_region = os.getenv('AWS_REGION')

# Debugging prints to verify environment variables
print("AWS credentials and region are set" if aws_access_key and aws_secret_key and aws_region else "AWS credentials and region are not set")

if not aws_access_key or not aws_secret_key or not aws_region:
    raise ValueError("AWS credentials and region must be set in environment variables")

# Create session
session = Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Create rekognition client
rekognition_client = session.client('rekognition')

@bp.route('/', methods=['POST'])
def compare_faces():
    data = request.get_json()
    gallery_id = data.get('gallery_id')
    image_data = data.get('image')

    if not gallery_id or not image_data:
        return jsonify({'error': 'Gallery ID and image data are required'}), 400

    try:
        image_data = base64.b64decode(image_data.split(",")[1])
    except Exception as e:
        return jsonify({'error': 'Invalid image data'}), 400

    photos = Photo.query.filter_by(gallery_id=gallery_id).all()
    matching_photos = []

    for photo in photos:
        try:
            response = rekognition_client.compare_faces(
                SourceImage={'Bytes': image_data},
                TargetImage={'S3Object': {'Bucket': current_app.config['S3_BUCKET'], 'Name': photo.filename}},
                SimilarityThreshold=90
            )
            if response['FaceMatches']:
                matching_photos.append(photo)
        except Exception as e:
            print(f"Error comparing faces: {e}")
            continue

    return jsonify([photo.to_dict() for photo in matching_photos]), 200

@bp.route('/health-check', methods=['GET'])
def health_check():
    try:
        rekognition_client.list_collections()
        return jsonify({'status': 'Connection to AWS Rekognition successful'}), 200
    except boto3.exceptions.NoCredentialsError as e:
        return jsonify({'status': 'Connection to AWS Rekognition failed', 'error': 'No AWS credentials found'}), 500
    except Exception as e:
        return jsonify({'status': 'Connection to AWS Rekognition failed', 'error': str(e)}), 500