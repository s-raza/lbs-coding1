from app import create_app
from app.init_data import add_data
from app.models import db
from app.settings import cfg

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_data(cfg.init_data.num_meters, cfg.init_data.num_meter_readings)
    app.run(host=cfg.app.host, port=cfg.app.port, debug=cfg.app.debug)
