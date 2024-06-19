
import pytest
from io import BytesIO
from app import create_app, db
from app.models import Gallery, Photo

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_upload_image(client):
    data = {'gallery_id': 1}
    file = (BytesIO(b'my file contents'), 'test.jpg')
    response = client.post('/api/image', data={'file': file, 'gallery_id': 1}, content_type='multipart/form-data')
    assert response.status_code == 201
    assert response.json['filename'] == 'test.jpg'

def test_filter_images(client):
    file = (BytesIO(b'my file contents'), 'test.jpg')
    response = client.post('/api/image/filter', data={'file': file}, content_type='multipart/form-data')
    assert response.status_code == 200
    assert isinstance(response.json, list)
