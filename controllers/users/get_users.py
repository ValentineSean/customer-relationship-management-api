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
        users = User.find(User.record_status=="ALIVE").all()
        
        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "users_retrieved_ok",
            "data": users
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_retrieve_users",
            "data": {},
        })