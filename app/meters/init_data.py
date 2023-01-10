import random
from typing import List

from faker import Faker

from app.settings import cfg

from .models import Meter, MeterData, db


def add_meter_data(meter_id: int, num_meter_readings: int) -> None:
    if num_meter_readings > cfg.init_data.max_meter_readings:
        num_meter_readings = cfg.init_data.max_meter_readings

    if num_meter_readings < cfg.init_data.min_meter_readings:
        num_meter_readings = cfg.init_data.min_meter_readings

    fake = Faker()
    Faker.seed(0)
    meter_data: List[MeterData] = []

    for _ in range(num_meter_readings):
        meter_data.append(
            MeterData(
                meter_id=meter_id,
                timestamp=fake.date_time_between(),
                value=round(random.uniform(1, 1000), 2),
            )
        )

    db.session.add_all(meter_data)
    db.session.flush()


def add_data(num_meters: int, num_meter_readings: int) -> None:
    if num_meters > cfg.init_data.max_meters:
        num_meters = cfg.init_data.max_meters

    if num_meters < cfg.init_data.min_meters:
        num_meters = cfg.init_data.min_meters

    for i in range(1, num_meters + 1):
        meter = Meter(label=f"Meter_{i}")
        db.session.add(meter)
        db.session.flush()
        add_meter_data(i, num_meter_readings)

    db.session.commit()
