from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from app import routes
        from app import utils

        db.create_all()

        user = utils.Migrate(app.config["USER_DATA_PATH"], routes.models.User)
        order = utils.Migrate(app.config["ORDER_DATA_PATH"], routes.models.Order)
        offer = utils.Migrate(app.config["OFFER_DATA_PATH"], routes.models.Offer)
        user.insert_to_base()
        order.insert_to_base()
        offer.insert_to_base()

        return app
