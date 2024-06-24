from app.users import bp
from apiflask import APIBlueprint, abort
from flask import redirect, url_for, session, request, current_app, jsonify
from authlib.integrations.flask_client import OAuth
from app.extensions import db
from app.models.user import UsersModel, UsersIn, UsersOut, LoginIn, TokenOut
import logging
from urllib.parse import urlencode, quote_plus
from app import oauth

logging.basicConfig(level=logging.DEBUG)

@bp.before_app_request
def setup_oauth():
    if not hasattr(oauth, 'okta'):
        oauth.register(
            "okta",
            client_id=current_app.config['OKTA_CLIENT_ID'],
            client_secret=current_app.config['OKTA_CLIENT_SECRET'],
            client_kwargs={
                "scope": "openid profile email",
            },
            server_metadata_url=f'https://{current_app.config["OKTA_DOMAIN"]}/.well-known/openid-configuration',
        )

@bp.route('/login', methods=['GET'])
def login():
    redirect_uri = url_for("users.auth_callback", _external=True)
    logging.debug(f"Redirecting to Okta for authorization with redirect URI: {redirect_uri}")
    return oauth.okta.authorize_redirect(redirect_uri)

@bp.route('/authorization-code/callback', methods=['GET', 'POST'])
def auth_callback():
    try:
        token = oauth.okta.authorize_access_token()
        logging.debug(f"Token received: {token}")
        user_info = token['userinfo']
        session["user"] = user_info
        return redirect(url_for('users.home'))
    except Exception as e:
        logging.error(f"OAuth Error: {str(e)}")
        logging.debug(f"Request args: {request.args}")
        logging.debug(f"Request form: {request.form}")
        return jsonify({"error": "Authorization failed"}), 400

@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(
        f'https://{current_app.config["OKTA_DOMAIN"]}/oauth2/v1/logout?'
        + urlencode(
            {
                "returnTo": url_for("users.home", _external=True),
                "client_id": current_app.config["OKTA_CLIENT_ID"],
            },
            quote_via=quote_plus,
        )
    )

@bp.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the home page",
        "user": session.get("user")
    })

@bp.route('/protected', methods=['GET'])
def protected():
    if 'user' not in session:
        abort(401, message="Unauthorized")
    user = session.get('user')
    return {'message': f'Hello, {user["name"]}!'}

@bp.route('/view_users', methods=['GET'])
@bp.output(UsersOut(many=True))
def view_users():
    users = UsersModel.query.all()
    return users