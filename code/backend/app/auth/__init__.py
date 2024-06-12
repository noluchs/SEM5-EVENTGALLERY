from apiflask import APIBlueprint

auth_bp = APIBlueprint('auth', __name__)

from app.auth import routes
