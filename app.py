from flask import Flask

from database import db
from init_data import add_data

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lbs.sqlite3"

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_data()
    app.run(debug=True)
