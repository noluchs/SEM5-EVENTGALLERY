import pytest
from app import create_app
from app.extensions import TestingConfig, db

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_app(app):
    assert app is not None
    assert app.config['TESTING'] == True

def test_root_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Eventgallery Backend'}

def test_health_check_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'
    assert response.json['database'] == 'connected'

def test_test_db_endpoint(client):
    response = client.get('/test-db')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Datenbankverbindung erfolgreich!'

def test_blueprints_registered(app):
    assert 'gallery' in [bp.name for bp in app.blueprints.values()]
    assert 'image' in [bp.name for bp in app.blueprints.values()]
    assert 'facerecognition' in [bp.name for bp in app.blueprints.values()]

def test_blueprint_urls(app):
    rules = [str(rule) for rule in app.url_map.iter_rules()]
    assert '/api/gallery/' in rules
    assert '/api/image/' in rules
    assert '/api/rekognition/' in rules