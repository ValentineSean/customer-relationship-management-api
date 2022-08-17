from flask import Blueprint, jsonify

from app import socketio

login_blueprint = Blueprint("login_blueprint", __name__)

@login_blueprint.route("/login")
def login():
    return "This is login page"

# WEB SOCKETS
socketio.on("my-event")
def handle_my_event(json, methods=["GET", "POST"]):
    print(f"received my event: {str(json)}")
    socketio.emit("my-response")