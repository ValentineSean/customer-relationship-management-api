import traceback
from flask_socketio import leave_room, emit
from app import socketio

# LEAVE ROOM EVENTS
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

        # send(f"{first_name} {last_name} has left the room.", to=issue_id)

        leave_room_success = {
            "status_code": "200",
            "status": "success",
            "message": "room_left_ok",
            "data": user
        }

        emit("leave-room-response-one", leave_room_success)
        socketio.emit("leave-room-response", leave_room_success)

    except:
        traceback.print_exc()

        join_room_error = {
            "status_code": "500",
            "status": "error",
            "message": "failed_to_leave_room",
            "data": user
        }

        emit("leave-room-response", join_room_error)