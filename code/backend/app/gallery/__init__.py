from apiflask import APIBlueprint

bp = APIBlueprint('gallery', __name__)

from app.gallery import routes
