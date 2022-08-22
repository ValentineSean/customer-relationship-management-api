import json
import jsons
import traceback

from flask import Blueprint, jsonify
from bson.json_util import dumps
from models.users import User
from config.database import redis_client_three

get_users_blueprint = Blueprint("get_users_blueprint", __name__)

@get_users_blueprint.route("/get-users")
def get_users():
    try:
        # users = User.find(User.pk=="01GB0GJMFW55092JF8AENK588Y")
        users = User.find().all()
        # print(f"users: {users}")
        # users = jsons.dump(users)
        # users = User(first_name="John", last_name="Doe", role="*", created_at="*")
        # print(f"users: {users}")
        # users = json.loads(dumps(users))
        # users = (users.dict())
        # users = User.get(pk="01GB0GJMFW55092JF8AENK588Y")
        # users = User.get(last_name="Doe")
        # users = User.get()
        # users = User.all_pks()
        # users = redis_client_three.json().get("users")
        # users = redis_client_three.mget("users")
        print(f"users: {users}")
        return "This is get users page"

    except:
        traceback.print_exc()
        return "Failed to GET users"