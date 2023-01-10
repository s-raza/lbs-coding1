from flask import render_template

from app import app
from models import Meter


@app.route("/meters/")
def all_meters() -> str:
    return render_template("meters.html", meters=Meter.find_all())
