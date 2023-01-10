from app import create_app
from app.init_data import add_data
from app.models import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_data()
    app.run(debug=True)
