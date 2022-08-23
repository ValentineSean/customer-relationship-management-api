import traceback

from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from models.users import User

login_blueprint = Blueprint("login_blueprint", __name__)

@login_blueprint.route("/login")
def login():
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    try:
        user = User.find((User.first_name==first_name)&(User.last_name==last_name)&(User.record_status=="ALIVE")).all()
        # users = j.dumps(users, iterable_as_array=True)

        if user:
            for u in user:
                user_dict = {}
                
                for x in u:
                    user_dict[x[0]] = x[1]
                # users_list.append(user_dict)
        
            return jsonify({
                "status_code": "200",
                "status": "success",
                "message": "users_retrieved_ok",
                "data": user_dict
            })

        else:
            return jsonify({
                "status_code": "500",
                "status": "error",
                "message": "user_not_found",
                "data": {}
            })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_retrieve_users",
            "data": [],
        })