import traceback
import json
import pandas as pd

from flask import Blueprint, jsonify
from redis_om import Migrator
from config.database import redis_client
from models.issues import Issue

get_issues_blueprint = Blueprint("get_issues_blueprint", __name__)

@get_issues_blueprint.route("/get-issues")
def get_issues():
    # Migrator().run()
    # issues = redis_client.lrange(name="issues", start=0, end=-1)
    issues = Issue.find().all()
    print(f"Issues: {issues}")
    return "This is get issues page"