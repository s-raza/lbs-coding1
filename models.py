from datetime import datetime

from database import db


class Meter(db.Model):
    __tablename__ = "meters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(), nullable=False)

    meter_data = db.relationship("MeterData", back_populates="meter")

    def __repr__(self) -> str:
        return f"Meter(id: {self.id}, label: {self.label})"


class MeterData(db.Model):
    __tablename__ = "meter_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    value = db.Column(db.Float, nullable=False)

    meter_id = db.Column(db.Integer, db.ForeignKey("meters.id"), nullable=False)
    meter = db.relationship("Meter", back_populates="meter_data")
