from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

# CONFIGURATIONS
# from ..config.security import jwt
# from ..config.security import jwt_secret_key

# BLUEPRINTS

# Auth
from controllers.auth.login import login_blueprint
from controllers.auth.register import register_blueprint

# Issues
from controllers.issues.get_issues import get_issues_blueprint
from controllers.issues.add_issue import add_issue_blueprint

app = Flask(__name__)
app.config["SECRET_KEY"] = "tjudiol!mèlkrif"

# socketio = SocketIO(app, cors_allowed_origins="*")
socketio = SocketIO()

CORS(app)

# EVENTS
from events import queuing_events

# app.config["JWT_SECRET_KEY"] = jwt_secret_key
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 604800
# jwt.init_app(app)

def create_app():
    # Auth
    app.register_blueprint(login_blueprint)
    app.register_blueprint(register_blueprint)

    # Issues
    app.register_blueprint(get_issues_blueprint)
    app.register_blueprint(add_issue_blueprint)

    socketio.init_app(app, cors_allowed_origins="*")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=True)