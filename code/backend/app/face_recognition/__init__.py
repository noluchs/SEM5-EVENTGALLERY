from flask import Blueprint

face_recognition_bp = Blueprint('face_recognition', __name__)

from app.face_recognition import routes

