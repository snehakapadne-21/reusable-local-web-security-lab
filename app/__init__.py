import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .routes import bp

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    if not app.config["SECRET_KEY"]:
        raise RuntimeError("SECRET_KEY must be configured")

    csrf.init_app(app)
    app.register_blueprint(bp)

    return app
