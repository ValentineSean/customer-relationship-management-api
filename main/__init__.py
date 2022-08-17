from flask import Flask, jsonify
from flask_cors import CORS

# CONFIGURATIONS
# from ..config.security import jwt
# from ..config.security import jwt_secret_key

# BLUEPRINTS
from ..controllers.auth import auth_blueprint

app = Flask(__name__)

CORS(app)

# app.config["JWT_SECRET_KEY"] = jwt_secret_key
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 604800
# jwt.init_app(app)

def create_app():
    app.register_blueprint(auth_blueprint)

    return app

app = create_app()