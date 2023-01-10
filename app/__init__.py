from flask import Flask

from .meters.models import db
from .meters.routes import meters_bp
from .settings import cfg


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{cfg.db.sqlite_file_name}"
    db.init_app(app)
    app.register_blueprint(meters_bp)

    return app
