from apiflask import APIBlueprint

bp = APIBlueprint('rekognition', __name__)

from app.facerecognition import routes

