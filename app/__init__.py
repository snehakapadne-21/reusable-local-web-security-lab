import os
from flask import Flask
from .routes import bp


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY",
        "local-development-secret"
    )

    app.register_blueprint(bp)

    return app
