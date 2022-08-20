import traceback

from flask import Blueprint, jsonify
from models.users import User

get_users_blueprint = Blueprint("get_users_blueprint", __name__)

@get_users_blueprint.route("/get-users")
def get_users():
    try:
        users = User.find().all()
        print(f"users: {users}")
        return "This is get users page"

    except:
        traceback.print_exc()
        return "Failed to GET users"