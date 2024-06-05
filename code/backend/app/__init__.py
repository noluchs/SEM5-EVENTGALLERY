from flask import Flask
from app.extensions import db
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from app.auth.routes import auth_bp
        from app.gallery.routes import gallery_bp
        from app.image.routes import image_bp
        from app.face_recognition.routes import face_recognition_bp

        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(gallery_bp, url_prefix='/gallery')
        app.register_blueprint(image_bp, url_prefix='/image')
        app.register_blueprint(face_recognition_bp, url_prefix='/face_recognition')

    return app


