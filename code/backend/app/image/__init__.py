from apiflask import APIBlueprint

image_bp = APIBlueprint('image', __name__)

from app.image import routes
