import json
import traceback
import pytz

from datetime import datetime
from flask_socketio import emit, join_room, leave_room
from app import socketio
from models.issues import Issue

# JSON File

# WEB SOCKET EVENTS
@socketio.on("change-issue-status")
def change_issue_status(issue):
    issue_id = issue["issue_id"]
    issue_status = issue["issue_status"]

    try:
        updated_issue = Issue().get(issue_id)

        updated_issue.issue_status = issue_status

        issue_pk = updated_issue.pk

        updated_issue.save()

        updated_issue_dict = {
            "pk": issue_pk,
            "sender": updated_issue.sender,
            "subject": updated_issue.subject,
            "description": updated_issue.description,
            "issue_status": updated_issue.issue_status,
            "created_at": updated_issue.created_at,
            "record_status": updated_issue.record_status,
        }

        updated_issue_json = {
            "status_code": "200",
            "status": "success",
            "message": "issue_added_ok",
            "data": updated_issue_dict,
        }

        print(f"received change issue status event")

        socketio.emit("change-issue-status-response", updated_issue_json)

    except:
        traceback.print_exc()
        
        issue_error_dict = {
            "status_code": "500",
            "status": "error",
            "message": "failed_to_change_issue_status"
        }

        emit("change-issue-status-response", issue_error_dict)