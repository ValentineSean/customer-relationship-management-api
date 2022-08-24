import json
import traceback
import pytz

from datetime import datetime
from flask import Blueprint, request, jsonify
from models.users import User

update_user_blueprint = Blueprint("update_user_blueprint", __name__)

@update_user_blueprint.route("/update-user", methods=["PUT"])
def update_user():
    user = request.json
    user_id = user["user_id"]
    first_name = user["first_name"]
    last_name = user["last_name"]
    role = user["role"]
    
    try:
        updated_user = User().get(user_id)

        updated_user.first_name = first_name
        updated_user.last_name = last_name
        updated_user.role = role

        user_pk = updated_user.pk

        updated_user.save()

        updated_user_dict = {
            "pk": user_pk,
            "first_name": updated_user.first_name,
            "last_name": updated_user.last_name,
            "role": updated_user.role,
            "created_at": updated_user.created_at,
            "role": updated_user.role,
        }

        print(f"UPDATED USER: {updated_user_dict}")
        
        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "user_updated_ok",
            "data": updated_user_dict
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_update_user",
            "data": {},
        })