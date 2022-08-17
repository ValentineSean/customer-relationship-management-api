from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

# CONFIGURATIONS
# from ..config.security import jwt
# from ..config.security import jwt_secret_key

app = Flask(__name__)
app.config["SECRET_KEY"] = "tjudiol!mèlkrif"

socketio = SocketIO(app)
CORS(app)

# BLUEPRINTS
from ..controllers.auth import auth_blueprint

# app.config["JWT_SECRET_KEY"] = jwt_secret_key
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 604800
# jwt.init_app(app)

def create_app():
    app.register_blueprint(auth_blueprint)

    return app

app = create_app()