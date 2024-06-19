from apiflask import APIBlueprint

bp = APIBlueprint('image', __name__)

from app.image import routes
