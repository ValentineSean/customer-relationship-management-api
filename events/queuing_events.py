from flask_socketio import emit, join_room, leave_room
from app import socketio

# JSON File
from read_json import json_data

# WEB SOCKET EVENTS
@socketio.on("get-issues")
def get_issues():
    print(f"received get issues event")
    emit("get-issues-response", json_data)