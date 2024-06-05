from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import boto3
import os
from dotenv import load_dotenv
from PIL import Image
import io
from app.face_recognition.recognition_utils import resize_image, compare_faces

load_dotenv("aws.env")

face_recognition_bp = Blueprint('face_recognition', __name__)

s3 = boto3.client("s3",
    region_name=os.environ.get("REGION"),
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
)

@face_recognition_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)

    # Resize the image before uploading to S3
    image = resize_image(file)
    image_io = io.BytesIO()
    image.save(image_io, format='JPEG')
    image_io.seek(0)

    s3.upload_fileobj(image_io, os.environ.get("UPLOAD_BUCKET"), filename)
    matches = compare_faces(filename)
    if not matches:  # Check if matches list is empty
        return jsonify({"message": "Kein Match gefunden"}), 200
    return jsonify({"matches": matches}), 200
