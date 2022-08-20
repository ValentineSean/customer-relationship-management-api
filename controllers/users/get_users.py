import traceback

from flask import Blueprint, jsonify
from models.users import User
from config.database import redis_client_three

get_users_blueprint = Blueprint("get_users_blueprint", __name__)

@get_users_blueprint.route("/get-users")
def get_users():
    try:
        # users = User.find(User.pk=="01GAXV62RH72X0YGJXHSWZC3JK").all()
        # users = User.get(pk="01GAXV62RH72X0YGJXHSWZC3JK")
        # users = User.all_pks()
        users = redis_client_three.json().get("users:1")
        print(f"users: {users}")
        return "This is get users page"

    except:
        traceback.print_exc()
        return "Failed to GET users"