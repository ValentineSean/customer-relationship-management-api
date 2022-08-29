import traceback
import pytz

from datetime import datetime
from flask_socketio import emit
from app import socketio
from models.messages import Message

# SEND MESSAGE EVENTS
@socketio.on("send-message")
def send_message(message):
    issue = message["issue"]
    sender = message["sender"]
    issue_data = message["issue_data"]
    sender_data = message["sender_data"]
    message_body = message["message_body"]
    message_status = "SENT"
    record_status = "ALIVE"

    zone = "Africa/Harare"
    timezone = pytz.timezone(zone)

    created_at_naive = datetime.now()
    created_at = created_at_naive.astimezone(timezone)
    created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")

    issue_data["pk"] = issue
    sender_data["pk"] = sender

    try:
        new_message = Message(
            issue = issue,
            sender = sender,
            issue_data = issue_data,
            sender_data = sender_data,
            message_body = message_body,
            message_status = message_status,
            created_at = created_at,
            record_status=record_status,
        )

        # delattr(new_message, "db_write")

        message_pk = new_message.pk

        new_message.save()

        new_message_dict = {
            "status_code": "200",
            "status": "success",
            "message": "message_added_ok",
            "data": {
                "pk": message_pk,
                "issue": issue,
                "sender": sender,
                "issue_data": issue_data,
                "sender_data": sender_data,
                "message_body": message_body,
                "message_status": message_status,
                "created_at": created_at,
                "record_status": record_status,
            }
        }

        print(f"received send message event")

        # socketio.emit("receive-message", new_message_dict, room=issue)
        socketio.emit("receive-message", new_message_dict)

    except:
        traceback.print_exc()
        
        message_error_dict = {
            "status_code": "500",
            "status": "error",
            "message": "failed_to_send_message"
        }

        emit("receive-message", message_error_dict)