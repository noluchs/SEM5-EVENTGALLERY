import pytest
from app import create_app

# Initialize the testing environment

@pytest.fixture
def client():
    app = create_app('testing')
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        yield app.test_client()