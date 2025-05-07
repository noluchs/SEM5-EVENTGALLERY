from flask import Flask
from .api import face_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(face_bp)
    return app