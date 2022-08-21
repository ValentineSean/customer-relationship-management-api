import traceback
import pytz

from datetime import datetime
from flask import Blueprint, request, jsonify
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
            **{
                "first_name": first_name,
                "last_name": last_name,
                "role": role,
                "created_at": created_at
            }
        )

        new_user.save()

        print(f"Added user: {new_user}")
        print(f"Added user type: {type(new_user)}")
        print(f"Added user primary key: {new_user.pk}")
        return "This is Register user page"

    except:
        traceback.print_exc()
        
        return "Failed to register user"