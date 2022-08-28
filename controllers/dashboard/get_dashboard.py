import traceback

from flask import Blueprint, jsonify, request
from collections import Counter
from models.issues import Issue

get_dashboard_blueprint = Blueprint("get_dashboard_blueprint", __name__)

@get_dashboard_blueprint.route("/get-dashboard")
def get_dashboard():
    customer_id = request.args.get("customer_id")

    try:
        if customer_id:
            issues = Issue.find((Issue.sender==customer_id)&(Issue.record_status=="ALIVE")).all()

        else:
            issues = Issue.find(Issue.record_status=="ALIVE").all()        

        issues_list = []
        
        # JSONIFY REDIS DATA RESPONSE
        for issue in issues:
            issue_dict = {}
            
            for x in issue:
                issue_dict[x[0]] = x[1]
                
            issues_list.append(issue_dict)

        # GROUP ISSUES USING ISSUE STATUS
        issues_count = dict(Counter((x["issue_status"]) for x in issues_list))

        print(f"ISSUES DICT: {issues_count}")
        
        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "issues_retrieved_ok",
            "data": issues_count
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_retrieve_issues",
            "data": [],
        })