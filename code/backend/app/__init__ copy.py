from apiflask import APIFlask, Schema, APIBlueprint
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, validate
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify
from .config import Config

db = SQLAlchemy()



# Schemas
class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    date = fields.Date(required=True)

class GallerySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    photos = fields.List(fields.Nested(lambda: PhotoSchema(only=("id", "filename"))))

class PhotoSchema(Schema):
    id = fields.Int(dump_only=True)
    filename = fields.Str(required=True)
    gallery_id = fields.Int(load_only=True)
    gallery = fields.Nested(GallerySchema, dump_only=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1, max=150))
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))

# Blueprints and routes
gallery_bp = APIBlueprint('gallery', __name__)
image_bp = APIBlueprint('image', __name__)
auth_bp = APIBlueprint('auth', __name__)
user_bp = APIBlueprint('user', __name__)

@gallery_bp.route('/gallery', methods=['GET'])
def get_galleries():
    galleries = Gallery.query.all()
    schema = GallerySchema(many=True)
    return {'galleries': schema.dump(galleries)}

@image_bp.route('/image', methods=['POST'])
def upload_image():
    # Image upload logic here
    return {'message': 'Image uploaded'}

@auth_bp.route('/auth', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return {'message': 'User authenticated'}
    else:
        return {'message': 'Invalid credentials'}, 401

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    schema = UserSchema()
    user_data = schema.load(data)
    user = User(
        username=user_data['username'],
        email=user_data['email']
    )
    user.set_password(user_data['password'])
    db.session.add(user)
    db.session.commit()
    return schema.dump(user), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    schema = UserSchema(many=True)
    return jsonify(schema.dump(users))

# Application factory
def create_app():
    app = APIFlask(__name__)  # Use APIFlask instead of Flask
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables for our data models

    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(gallery_bp, url_prefix='/gallery')
    app.register_blueprint(image_bp, url_prefix='/image')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)