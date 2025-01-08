import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "my_super_secret_string"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:rootpassword@eventgallery-db:3306/eventgallery"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    S3_BUCKET = os.environ.get('S3_BUCKET')
    S3_KEY = os.environ.get('S3_KEY')
    S3_SECRET = os.environ.get('S3_SECRET')
    S3_LOCATION = f'http://{S3_BUCKET}.s3.amazonaws.com/'
    AWS_REGION = os.environ.get('AWS_REGION', 'eu-central-1')

    AWS_REKOGNITION_KEY= os.environ.get('AWS_REKOGNITION_KEY')
    AWS_REKOGNITION_SECRET = os.environ.get('AWS_REKOGNITION_SECRET')


    # Okta configuration
    OKTA_DOMAIN = os.environ.get('OKTA_DOMAIN')
    OKTA_CLIENT_ID = os.environ.get('OKTA_CLIENT_ID')
    OKTA_CLIENT_SECRET = os.environ.get('OKTA_CLIENT_SECRET')
    OKTA_REDIRECT_URI = os.environ.get('OKTA_REDIRECT_URI')




