import traceback

from datetime import datetime as dt
from flask import Blueprint, jsonify, request
from models.issues import Issue

get_issues_blueprint = Blueprint("get_issues_blueprint", __name__)

@get_issues_blueprint.route("/get-issues")
def get_issues():
    customer_id = request.args.get("customer_id")
    issue_status = request.args.get("issue_status")
    issues = []

    try:
        if customer_id:
            if issue_status == "OPEN":
                issues = Issue.find((Issue.sender==customer_id)&(Issue.issue_status=="OPEN")&(Issue.record_status=="ALIVE")).all()

            elif issue_status == "CLOSED":
                issues = Issue.find((Issue.sender==customer_id)&(Issue.issue_status=="CLOSED")&(Issue.record_status=="ALIVE")).all()

            elif issue_status == "PENDING":
                issues = Issue.find((Issue.sender==customer_id)&(Issue.issue_status=="PENDING")&(Issue.record_status=="ALIVE")).all()

            elif issue_status == "PROGRESS":
                issues = Issue.find((Issue.sender==customer_id)&(Issue.issue_status=="PROGRESS")&(Issue.record_status=="ALIVE")).all()

            else:
                issues = Issue.find((Issue.sender==customer_id)&(Issue.record_status=="ALIVE")).all()

        else:
            if issue_status == "OPEN":
                issues = Issue.find((Issue.issue_status=="OPEN")&(Issue.record_status=="ALIVE")).all()

            elif issue_status == "CLOSED":
                issues = Issue.find((Issue.issue_status=="CLOSED")&(Issue.record_status=="ALIVE")).all()

            elif issue_status == "PENDING":
                issues = Issue.find((Issue.issue_status=="PENDING")&(Issue.record_status=="ALIVE")).all()

            elif issue_status == "PROGRESS":
                issues = Issue.find((Issue.issue_status=="PROGRESS")&(Issue.record_status=="ALIVE")).all()

            else:
                issues = Issue.find(Issue.record_status=="ALIVE").all()

        issues_list = []

        for issue in issues:
            issue_dict = {}
            
            for x in issue:
                issue_dict[x[0]] = x[1]
                
            issues_list.append(issue_dict)

        issues_list = sorted(issues_list, key=lambda x: dt.strptime(x['created_at'], '%Y-%m-%d %H:%M:%S'))
        
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