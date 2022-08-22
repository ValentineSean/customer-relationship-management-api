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
    desciption = issue["description"]
    sender = issue["sender"]

    zone = "Africa/Harare"
    timezone = pytz.timezone(zone)

    created_at_naive = datetime.now()
    created_at = created_at_naive.astimezone(timezone)
    created_at = created_at.strftime("%Y-%m-%d %H:%M:%S")

    try:
        new_issue = Issue(
            subject = subject,
            description = desciption,
            issue_status = "OPEN",
            sender = sender,
            created_at = created_at,
            record_status="ALIVE",
            db_write = True
        )

        delattr(new_issue, "db_write")

        new_issue.save()

        # new_issue = Issue.get(new_issue.pk)

        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "issue_added_ok"
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_add_issue",
        })