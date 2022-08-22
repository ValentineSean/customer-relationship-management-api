import traceback

from flask import Blueprint, jsonify
from models.issues import Issue

get_issues_blueprint = Blueprint("get_issues_blueprint", __name__)

@get_issues_blueprint.route("/get-issues")
def get_issues():
    try:
        issues = Issue.find(Issue.record_status=="ALIVE").all()
        
        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "issues_retrieved_ok",
            "data": issues
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_retrieve_issues",
            "data": {},
        })