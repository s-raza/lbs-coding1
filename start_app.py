import time
from logging import INFO as loginfo

from sqlalchemy_utils.functions import database_exists

from app import create_app
from app.meters.init_data import add_data
from app.models import db
from app.settings import cfg

app = create_app()
app.logger.setLevel(loginfo)

if __name__ == "__main__":
    with app.app_context():
        if not database_exists(f"sqlite:///instance/{cfg.db.sqlite_file_name}"):
            app.logger.info(f"Creating database: {cfg.db.sqlite_file_name}")
            start_time = time.time()
            db.create_all()
            app.logger.info(
                f"Inserting meter data: meters: {cfg.init_data.num_meters}, "
                f"readings per meter: {cfg.init_data.num_meter_readings}"
            )
            add_data(cfg.init_data.num_meters, cfg.init_data.num_meter_readings)
            end_time = round(time.time() - start_time, 2)
            app.logger.info(f"Database created, meter data inserted in {end_time}s")
    app.run(host=cfg.app.host, port=cfg.app.port, debug=cfg.app.debug)
