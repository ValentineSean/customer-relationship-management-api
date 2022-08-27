import json
import traceback
import pytz

from datetime import datetime
from flask_socketio import send, join_room, emit
from app import socketio
# from models.messages import Message

# JSON File

# SEND MESSAGE EVENTS

@socketio.on("join-room")
def on_join_room(user):
    # user_id = user["user_id"]
    issue_id = user["issue_id"]
    first_name = user["first_name"]
    last_name = user["last_name"]

    try:
        print(f"received join room event")

        join_room(issue_id)

        # socketio.emit("receive-message", new_message_dict)

        # send(f"{first_name} {last_name} has entered the room.", to=issue_id)

        join_room_success = {
            "status_code": "200",
            "status": "success",
            "message": "room_joined_ok",
            "data": user
        }

        socketio.emit("join-room-response", join_room)

    except:
        traceback.print_exc()

        join_room_error = {
            "status_code": "500",
            "status": "error",
            "message": "failed_to_join_room",
            "data": user
        }

        emit("join-room-response", join_room_error)