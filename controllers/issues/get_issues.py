import traceback
import json
import pandas as pd

from flask import Blueprint, jsonify
from flask_cors import cross_origin
from config.database import redis_client

get_issues_blueprint = Blueprint("get_issues_blueprint", __name__)

@get_issues_blueprint.route("/get-issues")
def get_issues():
    issues = redis_client.lrange(name="issues", start=0, end=-1)
    # issues = pd.DataFrame(map(json.loads, issues))
    print(f"Issues: {issues}")
    return "This is get issues page"