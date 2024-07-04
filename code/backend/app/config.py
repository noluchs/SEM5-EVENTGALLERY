import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_super_secret_string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') #or 'sqlite:///' + os.path.join(basedir, 'app.db')
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




class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    WTF_CSRF_ENABLED = False

config = {
    'default': Config,
    'testing': TestingConfig
}