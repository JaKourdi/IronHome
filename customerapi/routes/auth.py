import os

from flask import Blueprint
from flask import session, request
import jwt

import logging

from models.user import User
from utils.validate import validate_username_and_password

bp = Blueprint("auth", __name__, url_prefix="/auth")
logger = logging.getLogger(__name__)


# validator functions are used to validate input for user mgmt + login flows
# instead of marshmallow Schema as it doesn't have regex
# easier for me to validate these field with regex and apply constraints.

@bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        # validate input
        is_validated = validate_username_and_password(data.get('username'), data.get('password'))
        if is_validated is not True:
            return dict(message='Invalid data', data=None, error=is_validated), 400
        user = User().login(
            data["username"],
            data["password"]
        )
        if user:
            try:
                # default b token should expire after 24 hrs
                secret_key = os.environ.get('SECRET_KEY', 'dev-secret')
                user["token"] = jwt.encode(
                    {"user_id": user["_id"]},
                    secret_key,
                    algorithm="HS256"
                )
                return {
                    "message": "Successfully fetched auth token",
                    "data": user
                }
            except Exception as e:
                return {
                    "error": "Something went wrong",
                    "message": str(e)
                }, 500
        return {
            "message": "Error fetching auth token!, invalid username or password",
            "data": None,
            "error": "Unauthorized"
        }, 404
    except Exception as e:
        return {
            "message": "Something went wrong!",
            "error": str(e),
            "data": None
        }, 500
