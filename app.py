from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

# BLUEPRINTS

# Auth
from controllers.auth.login import login_blueprint
from controllers.auth.register_user import register_user_blueprint

# Users
from controllers.users.get_users import get_users_blueprint
from controllers.users.update_user import update_user_blueprint

# Issues
from controllers.issues.get_issues import get_issues_blueprint
from controllers.issues.add_issue import add_issue_blueprint
from controllers.issues.change_issue_status import change_issue_status_blueprint

# Chat
from controllers.chat.get_messages import get_messages_blueprint

# Dashboard
from controllers.dashboard.get_dashboard import get_dashboard_blueprint

app = Flask(__name__)
app.config["SECRET_KEY"] = "tjudiol!mèlkrif"

# socketio = SocketIO(app, cors_allowed_origins="*")
socketio = SocketIO()

CORS(app)

# EVENTS
# Queue
from events.queue import add_issue
from events.queue import change_issue_status

# Chat
from events.chat import send_message
from events.chat import on_join_room
from events.chat import on_leave_room

# app.config["JWT_SECRET_KEY"] = jwt_secret_key
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 604800
# jwt.init_app(app)

def create_app():
    # Auth
    app.register_blueprint(login_blueprint)
    app.register_blueprint(register_user_blueprint)

    # Users
    app.register_blueprint(get_users_blueprint)
    app.register_blueprint(update_user_blueprint)

    # Issues
    app.register_blueprint(get_issues_blueprint)
    app.register_blueprint(add_issue_blueprint)
    app.register_blueprint(change_issue_status_blueprint)

    # Chat
    app.register_blueprint(get_messages_blueprint)

    # Dashboard
    app.register_blueprint(get_dashboard_blueprint)

    socketio.init_app(app, cors_allowed_origins="*")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=True)