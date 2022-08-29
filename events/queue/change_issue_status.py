import traceback

from flask_socketio import emit
from app import socketio
from models.issues import Issue

# CHANGE ISSUE STATUS EVENTS
@socketio.on("change-issue-status")
def change_issue_status(issue):
    issue_id = issue["issue_id"]
    old_issue_status = issue["old_issue_status"]
    new_issue_status = issue["new_issue_status"]

    try:
        updated_issue = Issue().get(issue_id)

        updated_issue.issue_status = new_issue_status

        issue_pk = updated_issue.pk

        updated_issue.save()

        updated_issue_dict = {
            "pk": issue_pk,
            "sender": updated_issue.sender,
            "subject": updated_issue.subject,
            "description": updated_issue.description,
            "old_issue_status": old_issue_status,
            "new_issue_status": updated_issue.issue_status,
            "created_at": updated_issue.created_at,
            "record_status": updated_issue.record_status,
        }

        updated_issue_json = {
            "status_code": "200",
            "status": "success",
            "message": "issue_status_changed_ok",
            "data": updated_issue_dict,
        }

        print(f"received change issue status event")

        socketio.emit("change-issue-status-response", updated_issue_json)

    except:
        traceback.print_exc()
        
        issue_error_dict = {
            "status_code": "500",
            "status": "error",
            "message": "failed_to_change_issue_status",
            "data": {},
        }

        emit("change-issue-status-response", issue_error_dict)