import boto3
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from apiflask import HTTPTokenAuth
from app.models.user import UsersModel

from jwt import decode, InvalidTokenError
from flask import current_app

import logging

token_auth = HTTPTokenAuth()

@token_auth.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)
    if not user:
        return False
    return user

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





