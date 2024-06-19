
import pytest
from app import create_app, db
from app.models.user import UsersModel

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

def test_view_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_view_user_by_id(client):
    # Create a user first
    user = UsersModel(username='testuser', email='test@example.com', password='password')
    db.session.add(user)
    db.session.commit()

    response = client.get(f'/users/{user.id}')
    assert response.status_code == 200
    assert response.json['username'] == 'testuser'

def test_create_user(client):
    data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'password'}
    response = client.post('/users/create', json=data)
    assert response.status_code == 201
    assert response.json['username'] == 'newuser'

def test_update_user(client):
    # Create a user first
    user = UsersModel(username='testuser', email='test@example.com', password='password')
    db.session.add(user)
    db.session.commit()

    data = {'email': 'updated@example.com'}
    response = client.patch(f'/users/{user.id}/edit', json=data)
    assert response.status_code == 200
    assert response.json['email'] == 'updated@example.com'

def test_delete_user(client):
    # Create a user first
    user = UsersModel(username='testuser', email='test@example.com', password='password')
    db.session.add(user)
    db.session.commit()

    response = client.delete(f'/users/{user.id}/delete')
    assert response.status_code == 200

    # Check that the user is deleted
    deleted_user = UsersModel.query.get(user.id)
    assert deleted_user is None

def test_user_login(client):
    # Create a user first
    user = UsersModel(username='testuser', email='test@example.com', password='password')
    db.session.add(user)
    db.session.commit()

    data = {'username': 'testuser', 'password': 'password'}
    response = client.post('/users/login', json=data)
    assert response.status_code == 200
    assert 'token' in response.json
