import json
import traceback
import pytz

from datetime import datetime
from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from models.users import User

register_user_blueprint = Blueprint("register_user_blueprint", __name__)

@register_user_blueprint.route("/register-user", methods=["POST"])
def register_user():
    user = request.json
    first_name = user["first_name"]
    last_name = user["last_name"]
    role = user["role"]

    zone = "Africa/Harare"
    timezone = pytz.timezone(zone)

    created_at_naive = datetime.now()
    created_at = created_at_naive.astimezone(timezone)
    created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            role=role,
            created_at=created_at,
            record_status="ALIVE",
            db_write = True
        )
        
        delattr(new_user, "db_write")

        new_user.save()

        # new_user = User.get(new_user.pk)
        
        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "user_registered_ok"
        })

    except:
        traceback.print_exc()
        
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_register_user",
        })