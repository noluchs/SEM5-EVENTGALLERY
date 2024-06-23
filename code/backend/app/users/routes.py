from app.users import bp
from apiflask import abort as flask_abort
from app.extensions import db, token_auth
from app.models.user import UsersModel, UsersIn, UsersOut, LoginIn, TokenOut
import logging

logging.basicConfig(level=logging.DEBUG)

# get all users
@bp.get('/')
@bp.output(UsersOut(many=True))
def view_users(database_table=UsersModel):
    return database_table.query.all()

# get user by id
@bp.get('/<int:user_id>')
@bp.auth_required(token_auth)
@bp.output(UsersOut)
def view_user_by_id(user_id, database_table=UsersModel):
    user = db.get_or_404(database_table, user_id)
    return user

# create new user
@bp.post('/create')
@bp.input(UsersIn, location='json')
@bp.output(UsersOut, status_code=201)
def create_user(json_data, database_table=UsersModel):
    password = json_data.pop('password')
    user = database_table(password=password, **json_data)
    db.session.add(user)
    db.session.commit()
    logging.debug(f"User created: {user.email} with raw password: {password} and hashed password: {user.password}")
    return user

# change the information for a db entry
@bp.patch('/<int:user_id>/edit')
@bp.auth_required(token_auth)
@bp.input(UsersIn(partial=True), location='json')
@bp.output(UsersOut)
def update_user(user_id, json_data, database_table=UsersModel):
    user = db.get_or_404(database_table, user_id)
    for key, value in json_data.items():
        insert_data = value
        if key == "password":
            insert_data = custom_generate_password_hash(value)
        setattr(user, key, insert_data)
    db.session.commit()
    return user

# remove user by id
@bp.delete('/<int:user_id>/delete')
@bp.auth_required(token_auth)
@bp.output(UsersOut(many=True))
def delete_user(user_id, database_table=UsersModel):
    user = db.get_or_404(database_table, user_id)
    db.session.delete(user)
    db.session.commit()
    return database_table.query.all()

# Login route
@bp.route('/login', methods=['POST', 'OPTIONS'])
@bp.input(LoginIn)
@bp.output(TokenOut)
def login(json_data):
    user = UsersModel.query.filter_by(email=json_data['email']).first()
    if user:
        logging.debug(f"Login attempt: user email: {json_data['email']}, entered password: {json_data['password']}, stored hash: {user.password}")
        password_check = user.check_password(json_data['password'])
        logging.debug(f"Password check result: {password_check}")
        if password_check:
            token = user.generate_auth_token()
            return {'token': token, 'duration': 600}
    flask_abort(401, message="Invalid email or password")