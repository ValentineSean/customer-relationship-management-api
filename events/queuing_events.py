import json
import uuid

from flask_socketio import emit, join_room, leave_room
from app import socketio
from config.database import redis_client

# JSON File
from read_json import json_data
from read_json import write_json

# WEB SOCKET EVENTS
@socketio.on("get-issues")
def get_issues():
    print(f"received get issues event")
    emit("get-issues-response", json_data)

@socketio.on("add-issue")
def add_issue():
    issue_id = uuid.uuid4().hex
    
    issue = {
        "id": issue_id,
        "subject": "SIM card is not working",
        "description": "Maybe its because ...",
        "handlers": [6, 7],
        "issue_status": "OPEN",
        "created_at": "2022-08-12"
    }

    issue = json.dumps(issue)

    print(f"received add issue event")

    added_issue = redis_client.rpush("issues", issue)
    print(added_issue)
    emit("add-issue-response", json_data)