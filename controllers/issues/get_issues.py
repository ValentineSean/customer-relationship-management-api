import traceback

from flask import Blueprint, jsonify, request
from models.issues import Issue

get_issues_blueprint = Blueprint("get_issues_blueprint", __name__)

@get_issues_blueprint.route("/get-issues")
def get_issues():
    customer_id = request.args.get("customer_id")
    issues = []

    try:
        if customer_id:
            issues = Issue.find((Issue.sender==customer_id)&(Issue.record_status=="ALIVE")).all()

        else:
            issues = Issue.find(Issue.record_status=="ALIVE").all()

        issues_list = []

        for issue in issues:
            issue_dict = {}
            
            for x in issue:
                issue_dict[x[0]] = x[1]
                
            issues_list.append(issue_dict)
        
        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "issues_retrieved_ok",
            "data": issues_list
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_retrieve_issues",
            "data": [],
        })