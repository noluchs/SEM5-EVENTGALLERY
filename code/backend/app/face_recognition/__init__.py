from apiflask import APIBlueprint

face_recognition_bp = APIBlueprint('face_recognition', __name__)

from app.face_recognition import routes

