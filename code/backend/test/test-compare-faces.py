import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from app.facerecognition import routes
from app.models import Photo

def test_compare_faces():
    # Create a test client using the Flask application
    app = Flask(__name__)
    with app.test_client() as client:
        # Mock the request.get_json() method
        with patch('flask.request.get_json') as mock_get_json:
            mock_get_json.return_value = {
                'gallery_id': 1,
                'image': 'data:image/jpeg;base64,/9...'
            }

            # Mock the Photo.query.filter_by().all() method
            with patch('app.models.Photo.query.filter_by') as mock_filter_by:
                mock_query = MagicMock()
                mock_filter_by.return_value = mock_query
                mock_query.all.return_value = []

                # Mock the rekognition_client.compare_faces method
                with patch('app.facerecognition.routes.rekognition_client.compare_faces') as mock_compare_faces:
                    mock_compare_faces.return_value = {'FaceMatches': []}

                    # Call the compare_faces function
                    response = client.post('/')

                    # Assert that the status code is 200
                    assert response.status_code == 200