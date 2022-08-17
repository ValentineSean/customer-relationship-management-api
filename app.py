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
from controllers.auth.login import login_blueprint
from controllers.auth.register import register_blueprint

# app.config["JWT_SECRET_KEY"] = jwt_secret_key
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 604800
# jwt.init_app(app)

def create_app():
    app.register_blueprint(login_blueprint)
    app.register_blueprint(register_blueprint)

    return app

app = create_app()

if __name__ == "__main__":
    # app.run(debug=True)
    socketio.run(app, debug=True)