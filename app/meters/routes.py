from flask import Blueprint, Response, jsonify, render_template

from app.models import Meter, MeterData

meters_bp = Blueprint("meters", __name__, template_folder="templates")


@meters_bp.route("/meters/")
def all_meters() -> str:
    _all = Meter.find_all()
    return render_template("meters.html", meters=_all)


@meters_bp.route("/meters/<meter_id>")
def meter_data(meter_id: int) -> Response:
    meter_data = MeterData.find_by_meter_id(meter_id=meter_id)
    if len(meter_data) == 0:
        return jsonify({"error": f"Meter with id {meter_id} not found"}), 404
    return jsonify(meter_data)
