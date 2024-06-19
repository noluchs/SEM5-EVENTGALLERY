
import pytest
from app import create_app, db
from app.models import Gallery

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

def test_get_galleries(client):
    response = client.get('/api/gallery')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_gallery(client):
    data = {'name': 'New Gallery'}
    response = client.post('/api/gallery', json=data)
    assert response.status_code == 201
    assert response.json['name'] == 'New Gallery'

def test_delete_gallery(client):
    # Create a gallery first
    gallery = Gallery(name='Gallery to Delete')
    db.session.add(gallery)
    db.session.commit()
    
    # Delete the gallery
    response = client.delete(f'/api/gallery/{gallery.id}')
    assert response.status_code == 204

    # Check that the gallery is deleted
    deleted_gallery = Gallery.query.get(gallery.id)
    assert deleted_gallery is None
