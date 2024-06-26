import pytest
from app import create_app, db
from app.models import Gallery, Photo

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
    # First create a gallery
    response = client.post('/gallery', json={'name': 'Test Gallery'})
    gallery_id = response.get_json()['id']

    # Add image to the gallery
    response = client.post(f'/gallery/{gallery_id}/photos', data={
        'file': (open('path_to_image.jpg', 'rb'), 'path_to_image.jpg')
    })
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['gallery_id'] == gallery_id

def test_face_recognition(client):
    # First create a gallery
    response = client.post('/gallery', json={'name': 'Test Gallery'})
    gallery_id = response.get_json()['id']

    # Add two images to the gallery
    client.post(f'/gallery/{gallery_id}/photos', data={
        'file': (open('path_to_image1.jpg', 'rb'), 'path_to_image1.jpg')
    })
    client.post(f'/gallery/{gallery_id}/photos', data={
        'file': (open('path_to_image2.jpg', 'rb'), 'path_to_image2.jpg')
    })

    # Use face recognition to compare images
    response = client.post(f'/facerecognition/compare', json={
        'gallery_id': gallery_id,
        'image_path': 'path_to_comparison_image.jpg'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'matches' in data