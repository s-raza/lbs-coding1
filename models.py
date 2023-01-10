from datetime import datetime
from typing import List

from database import db


class Meter(db.Model):
    __tablename__ = "meters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(), nullable=False)

    meter_data = db.relationship("MeterData", back_populates="meter")

    @classmethod
    def find_by_label(cls, label: str) -> "Meter":
        return cls.query.filter_by(label=label).first()

    @classmethod
    def find_by_id(cls, id: int) -> "Meter":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["Meter"]:
        return cls.query.all()

    def __repr__(self) -> str:
        return f"Meter(id: {self.id}, label: {self.label})"

    def __str__(self) -> str:
        return self.__repr__()


class MeterData(db.Model):
    __tablename__ = "meter_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    value = db.Column(db.Float, nullable=False)

    meter_id = db.Column(db.Integer, db.ForeignKey("meters.id"), nullable=False)
    meter = db.relationship("Meter", back_populates="meter_data")

    def __repr__(self) -> str:
        return (
            f"MeterData(id: {self.id}, "
            f"meter_id: {self.meter_id}, "
            f"timestamp: {self.timestamp}, "
            f"value: {self.value})"
        )

    def __str__(self) -> str:
        return self.__repr__()
