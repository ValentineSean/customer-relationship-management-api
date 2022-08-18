import traceback
import json
import pandas as pd

from flask import Blueprint, jsonify
from flask_cors import cross_origin
from config.database import redis_client
from models.issues import Issue

add_issue_blueprint = Blueprint("add_issue_blueprint", __name__)

@add_issue_blueprint.route("/add-issue", methods=["POST"])
def add_issue():
    my_issue = Issue(
        subject = "Poor network this side",
        description = "I dont know why...",
        sender = 8,
        handlers = "",
        issue_status = "OPEN",
        created_at = "2022-06-15"
    )

    my_issue.save()

    print(f"Added issue: {my_issue}")
    print(f"Added issue primary key: {my_issue.pk}")
    return "This is add issue page"