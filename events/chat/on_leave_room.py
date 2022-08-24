import json
import traceback
import pytz

from datetime import datetime
from flask_socketio import send, leave_room
from app import socketio
# from models.messages import Message

# JSON File

# SEND MESSAGE EVENTS

@socketio.on("leave-room")
def on_leave_room(user):
    # user_id = user["user_id"]
    issue_id = user["issue_id"]
    first_name = user["first_name"]
    last_name = user["last_name"]

    try:
        print(f"received leave room event")

        leave_room(issue_id)

        # socketio.emit("receive-message", new_message_dict)

        send(f"{first_name} {last_name} has left the room.", to=issue_id)

    except:
        traceback.print_exc()

        # emit("receive-message", message_error_dict)