from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from app import models
        from app import utils
        from offers import offers
        from orders import orders
        from users import users
        app.register_blueprint(offers, url_prefix='/offers')
        app.register_blueprint(orders, url_prefix='/orders')
        app.register_blueprint(users, url_prefix='/users')

        db.create_all()


        user = utils.Migrate(app.config["USER_DATA_PATH"], models.User)
        order = utils.Migrate(app.config["ORDER_DATA_PATH"], models.Order)
        offer = utils.Migrate(app.config["OFFER_DATA_PATH"], models.Offer)
        user.insert_to_base()
        order.insert_to_base()
        offer.insert_to_base()

        return app
