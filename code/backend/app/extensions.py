from flask_sqlalchemy import SQLAlchemy
import boto3

db = SQLAlchemy()

def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=current_app.config['S3_KEY'],
        aws_secret_access_key=current_app.config['S3_SECRET'],
        region_name=current_app.config['AWS_REGION']
    )

def get_rekognition_client():
    return boto3.client(
        'rekognition',
        aws_access_key_id=current_app.config['S3_KEY'],
        aws_secret_access_key=current_app.config['S3_SECRET'],
        region_name=current_app.config['AWS_REGION']
    )