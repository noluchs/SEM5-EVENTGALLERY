from apiflask import APIFlask
from flask_cors import CORS

from .extensions import db
from .config import Config


def create_app(config_class=Config):
    app = APIFlask(__name__)
    app.config.from_object(config_class)
    CORS(app, origins="http://localhost:3000")  # Allow CORS for your frontend server
    # Initialize Flask extensions here
    db.init_app(app)

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.gallery import bp as gallery_bp
    app.register_blueprint(gallery_bp, url_prefix='/api/gallery')

    from app.image import bp as image_bp
    app.register_blueprint(image_bp, url_prefix='/api/image')

    with app.app_context():
        db.create_all()

    @app.route('/')
    def test_page():
        return {'message': 'Eventgallery Backend'}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)