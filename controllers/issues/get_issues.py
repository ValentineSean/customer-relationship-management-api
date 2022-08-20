import traceback

from flask import Blueprint, jsonify
from models.issues import Issue

get_issues_blueprint = Blueprint("get_issues_blueprint", __name__)

@get_issues_blueprint.route("/get-issues")
def get_issues():
    try:
        issues = Issue.find().all()
        print(f"Issues: {issues}")
        return "This is get issues page"

    except:
        traceback.print_exc()
        return "Failed to GET issues"