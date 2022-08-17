from flask import Blueprint

from . import auth_blueprint

@auth_blueprint.route("/login")
def login():
    return "This is login page"