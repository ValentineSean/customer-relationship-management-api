import traceback

from flask import Blueprint, jsonify
from flask_cors import cross_origin

login_blueprint = Blueprint("login_blueprint", __name__)

@login_blueprint.route("/login")
def login():
    return "This is login page"