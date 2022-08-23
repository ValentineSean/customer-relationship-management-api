import json
import simplejson as j
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
        # users = j.dumps(users, iterable_as_array=True)
        users_list = []

        for user in users:
            user_dict = {}
            
            for x in user:
                user_dict[x[0]] = x[1]
                
            users_list.append(user_dict)
        
        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "users_retrieved_ok",
            "data": users_list
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_retrieve_users",
            "data": [],
        })