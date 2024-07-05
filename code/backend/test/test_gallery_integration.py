import pytest
from app import create_app, db
from app.extensions import TestingConfig
from app.models import Gallery, Photo
import io
import os

@pytest.fixture
def client():
    app = create_app(TestingConfig)  # Pass the TestingConfig class
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

def test_create_gallery(client):
    response = client.post('/api/gallery', json={'name': 'Test Gallery'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test Gallery'
    assert 'id' in data

def test_add_image_to_gallery(client):
    response = client.post('/api/gallery', json={'name': 'Test Gallery'})
    gallery_id = response.get_json()['id']

    image_path = os.path.join('backend/test/testfile', 'test_image.jpg')
    with open(image_path, 'rb') as image_data:
        response = client.post(f'/api/gallery/{gallery_id}/photos', content_type='multipart/form-data', data={
            'file': (image_data, 'test_image.jpg')
        })
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['gallery_id'] == gallery_id

