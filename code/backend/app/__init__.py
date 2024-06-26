from apiflask import APIFlask
from flask_cors import CORS
from .extensions import db
from .config import Config
import os
from flask_migrate import Migrate

migrate = Migrate()

def create_app(config_class=Config):
    app = APIFlask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints

    from .gallery import bp as gallery_bp
    app.register_blueprint(gallery_bp, url_prefix='/api/gallery')

    from .image import bp as image_bp
    app.register_blueprint(image_bp, url_prefix='/api/image')

    from .facerecognition import bp as face_recognition_bp
    app.register_blueprint(face_recognition_bp, url_prefix='/api/rekognition')

    with app.app_context():
        db.create_all()

    @app.route('/')
    def test_page():
        return {'message': 'Eventgallery Backend'}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)