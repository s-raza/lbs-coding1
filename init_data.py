import random
from typing import List

from faker import Faker

from database import db
from models import Meter, MeterData


def get_random_meter_data(max_meter_readings: int = 50) -> List[MeterData]:
    if max_meter_readings > 50:
        max_meter_readings = 50

    if max_meter_readings < 10:
        max_meter_readings = 10

    fake = Faker()
    Faker.seed(0)
    meter_data = []

    for _ in range(max_meter_readings):
        reading = {
            "timestamp": fake.date_time_between(),
            "value": round(random.uniform(1, 1000), 2),
        }
        meter_data.append(MeterData(**reading))

    return meter_data


def add_data(max_meters: int = 100, max_meter_readings: int = 50) -> None:
    if max_meters > 100:
        max_meters = 100

    if max_meters < 10:
        max_meters = 10

    to_add = []

    for i in range(1, max_meters + 1):
        entry = {
            "label": f"Meter_{i}",
            "meter_data": get_random_meter_data(max_meter_readings),
        }
        to_add.append(Meter(**entry))

    db.session.add_all(to_add)
    db.session.commit()
