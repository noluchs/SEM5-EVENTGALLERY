from apiflask import APIFlask
from .extensions import db
from .config import Config
from .routes import gallery_bp, image_bp


def create_app(config_class=Config):
    app = APIFlask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)


    app.register_blueprint(gallery_bp, url_prefix='/api')
    app.register_blueprint(image_bp, url_prefix='/api')


    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    with app.app_context():
        db.create_all()

    @app.route('/')
    def test_page():
        return {'message': 'Eventgallery Backend'}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)