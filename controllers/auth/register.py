from flask import Blueprint, jsonify

from app import socketio

register_blueprint = Blueprint("register_blueprint", __name__)

@register_blueprint.route("/register")
def register():
    return "This is register page"

# WEB SOCKETS
socketio.on("my-event")
def handle_my_event(json, methods=["GET", "POST"]):
    print(f"received my event: {str(json)}")
    socketio.emit("my-response")