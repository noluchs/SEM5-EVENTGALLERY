from apiflask import APIBlueprint

gallery_bp = APIBlueprint('gallery', __name__)

from app.gallery import routes
