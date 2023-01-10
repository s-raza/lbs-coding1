from flask import Flask

from app.meters.routes import meters_bp
from app.models import db
from app.settings import cfg


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = cfg.db.sqlite_url
    db.init_app(app)
    app.register_blueprint(meters_bp)

    return app
