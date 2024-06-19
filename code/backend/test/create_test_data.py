# Ensure create_test_data.py has the correct content
corrected_create_test_data_content = """
from app import db
from app.models.user import UsersModel

def create_test_data():
    # Add test data to the database
    user1 = UsersModel(username='testuser1', email='test1@example.com', password='password1')
    user2 = UsersModel(username='testuser2', email='test2@example.com', password='password2')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
"""

with open(create_test_data_file_path, 'w') as file:
    file.write(corrected_create_test_data_content)

# Ensure __init__.py has the correct content
updated_init_content = """
from test.create_test_data import create_test_data
"""

with open(init_file_path, 'w') as file:
    file.write(updated_init_content)