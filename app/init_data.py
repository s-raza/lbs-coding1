import random
from typing import List

from faker import Faker

from app.models import Meter, MeterData, db


def add_meter_data(meter_id: int, max_meter_readings: int = 50) -> None:
    if max_meter_readings > 50:
        max_meter_readings = 50

    if max_meter_readings < 10:
        max_meter_readings = 10

    fake = Faker()
    Faker.seed(0)
    meter_data: List[MeterData] = []

    for _ in range(max_meter_readings):
        meter_data.append(
            MeterData(
                meter_id=meter_id,
                timestamp=fake.date_time_between(),
                value=round(random.uniform(1, 1000), 2),
            )
        )

    db.session.add_all(meter_data)
    db.session.flush()


def add_data(max_meters: int = 100, max_meter_readings: int = 50) -> None:
    if max_meters > 100:
        max_meters = 100

    if max_meters < 10:
        max_meters = 10

    for i in range(1, max_meters + 1):
        meter = Meter(label=f"Meter_{i}")
        db.session.add(meter)
        db.session.flush()
        add_meter_data(i, max_meter_readings)

    db.session.commit()
