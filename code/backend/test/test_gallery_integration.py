import pytest
from app import create_app, db
from app.models import Gallery, Photo
import io
import os

@pytest.fixture
def client():
    app = create_app('testing')
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

def test_create_gallery(client):
    response = client.post('/gallery', json={'name': 'Test Gallery'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test Gallery'
    assert 'id' in data

def test_add_image_to_gallery(client):
    response = client.post('/gallery', json={'name': 'Test Gallery'})
    gallery_id = response.get_json()['id']

    image_path = os.path.join('backend/test/testfile', 'test_image.jpg')
    with open(image_path, 'rb') as image_data:
        response = client.post(f'/gallery/{gallery_id}/photos', content_type='multipart/form-data', data={
            'file': (image_data, 'test_image.jpg')
        })
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['gallery_id'] == gallery_id

def test_face_recognition(client, monkeypatch):
    class MockBoto3Client:
        def compare_faces(self, SourceImage, TargetImage):
            return {
                'FaceMatches': [{'Face': {'Confidence': 99.0}}]
            }

    monkeypatch.setattr('boto3.client', lambda *args, **kwargs: MockBoto3Client())

    response = client.post('/gallery', json={'name': 'Test Gallery'})
    gallery_id = response.get_json()['id']

    image_path1 = os.path.join('backend/test/testfile', 'test_image1.jpg')
    with open(image_path1, 'rb') as image_data1:
        client.post(f'/gallery/{gallery_id}/photos', content_type='multipart/form-data', data={
            'file': (image_data1, 'test_image1.jpg')
        })

    image_path2 = os.path.join('backend/test/testfile', 'test_image2.jpg')
    with open(image_path2, 'rb') as image_data2:
        client.post(f'/gallery/{gallery_id}/photos', content_type='multipart/form-data', data={
            'file': (image_data2, 'test_image2.jpg')
        })

    response = client.post('/facerecognition/compare', json={
        'gallery_id': gallery_id,
        'image_path': 'test_image1.jpg'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'matches' in data
    assert data['matches'] == [99.0]