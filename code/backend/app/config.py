import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_super_secret_string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    S3_BUCKET = os.environ.get('S3_BUCKET')
    S3_KEY = os.environ.get('S3_KEY')
    S3_SECRET = os.environ.get('S3_SECRET')
    S3_LOCATION = f'http://{S3_BUCKET}.s3.amazonaws.com/'
    AWS_REGION = os.environ.get('AWS_REGION')
    S3_REGION = os.getenv('S3_REGION', 'eu-central-1')

    S3_BUCKET_2="msvc-gallery"
    S3_REGION_2="eu-central-1"

    # Okta configuration
    OKTA_DOMAIN = os.environ.get('OKTA_DOMAIN')
    OKTA_CLIENT_ID = os.environ.get('OKTA_CLIENT_ID')
    OKTA_CLIENT_SECRET = os.environ.get('OKTA_CLIENT_SECRET')
    OKTA_REDIRECT_URI = os.environ.get('OKTA_REDIRECT_URI')
