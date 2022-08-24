import json
import traceback
import pytz

from datetime import datetime
from flask_socketio import emit, send, join_room, leave_room
from app import socketio
# from models.messages import Message

# JSON File

# SEND MESSAGE EVENTS

@socketio.on("join-room")
def join_room(user):
    # user_id = user["user_id"]
    issue_id = user["issue_id"]
    first_name = user["first_name"]
    last_name = user["last_name"]

    try:
        print(f"received send message event")

        join_room(issue_id)

        # socketio.emit("receive-message", new_message_dict)

        send(f"{first_name} {last_name} has entered the room.", to=issue_id)

    except:
        traceback.print_exc()

        # emit("receive-message", message_error_dict)