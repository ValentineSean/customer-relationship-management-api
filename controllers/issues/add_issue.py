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
            sender = sender,
            handlers = [],
            issue_status = "OPEN",
            created_at = created_at
        )

        new_issue.save()

        print(f"Added issue: {new_issue}")
        print(f"Added issue primary key: {new_issue.pk}")
        return "This is add issue page"

    except:
        traceback.print_exc()
        
        return "Failed to add new issue"