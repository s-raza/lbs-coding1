import logging

from sqlalchemy_utils.functions import database_exists

from app import create_app
from app.init_data import add_data
from app.models import db
from app.settings import cfg

app = create_app()
app.logger.setLevel(logging.INFO)

if __name__ == "__main__":
    with app.app_context():
        if not database_exists(f"sqlite:///instance/{cfg.db.sqlite_file_name}"):
            app.logger.info(f"Creating database: {cfg.db.sqlite_file_name}")
            db.create_all()
            app.logger.info(
                f"Inserting meter data:  meters: {cfg.init_data.num_meters}, "
                f"readings per meter: {cfg.init_data.num_meter_readings}"
            )
            add_data(cfg.init_data.num_meters, cfg.init_data.num_meter_readings)
            app.logger.info("Database created, meter data inserted")
    app.run(host=cfg.app.host, port=cfg.app.port, debug=cfg.app.debug)
