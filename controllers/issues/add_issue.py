import traceback
import pytz

from datetime import datetime
from flask import Blueprint, request, jsonify
from models.issues import Issue

add_issue_blueprint = Blueprint("add_issue_blueprint", __name__)

@add_issue_blueprint.route("/add-issue", methods=["POST"])
def add_issue():
    issue = request.json
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

        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "issue_added_ok",
            "data": new_issue_dict,
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_add_issue",
        })