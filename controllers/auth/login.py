from flask import jsonify

from . import auth_blueprint

from ...main.main import socketio

@auth_blueprint.route("/login")
def login():
    return "This is login page"

# WEB SOCKETS
socketio.on("my-event")
def handle_my_event(json, methods=["GET", "POST"]):
    print(f"received my event: {str(json)}")
    socketio.emit("my-response")