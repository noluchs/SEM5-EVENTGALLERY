import boto3
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from .config import Config



import logging
logging.getLogger('botocore').setLevel(logging.WARNING)
logging.getLogger('boto3').setLevel(logging.WARNING)




def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=current_app.config['S3_KEY'],
        aws_secret_access_key=current_app.config['S3_SECRET'],
        region_name=current_app.config['S3_REGION']
    )

def get_rekognition_client():
    return boto3.client(
        'rekognition',
        aws_access_key_id=current_app.config['S3_KEY'],
        aws_secret_access_key=current_app.config['S3_SECRET'],
        region_name=current_app.config['AWS_REGION']
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

