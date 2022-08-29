import traceback
import pytz

from datetime import datetime
from flask_socketio import emit
from app import socketio
from models.issues import Issue

# ADD ISSUE EVENTS
@socketio.on("add-issue")
def add_issue(issue):
    subject = issue["subject"]
    description = issue["description"]
    sender = issue["sender"]
    issue_status = "OPEN"
    record_status = "ALIVE"

    zone = "Africa/Harare"
    timezone = pytz.timezone(zone)

    created_at_naive = datetime.now()
    created_at = created_at_naive.astimezone(timezone)
    created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")

    try:
        new_issue = Issue(
            subject = subject,
            description = description,
            issue_status = issue_status,
            sender = sender,
            created_at = created_at,
            record_status=record_status,
        )

        # delattr(new_issue, "db_write")

        issue_pk = new_issue.pk

        new_issue.save()

        new_issue_dict = {
            "pk": issue_pk,
            "subject": subject,
            "description": description,
            "issue_status": issue_status,
            "sender": sender,
            "created_at": created_at,
            "record_status": record_status,
        }

        new_issue_json = {
            "status_code": "200",
            "status": "success",
            "message": "issue_added_ok",
            "data": new_issue_dict
        }

        print(f"received add issue event")

        socketio.emit("add-issue-response", new_issue_json)

    except:
        traceback.print_exc()
        
        issue_error_dict = {
            "status_code": "500",
            "status": "error",
            "message": "failed_to_add_issue",
            "data": {},
        }

        emit("add-issue-response", issue_error_dict)