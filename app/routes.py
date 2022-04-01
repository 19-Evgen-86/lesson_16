from flask import current_app as app, jsonify, abort, request

from app import models, db

# отображение данных(передача клиенту)
from app.utils import validate_json


@app.route("/users", methods=["GET"])
def get_users():
    users = db.session.query(models.User).all()
    return jsonify([user.serialize() for user in users])


@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    user = db.session.query(models.User).filter(models.User.id == id).first()

    if user is None:
        abort(404)

    return jsonify(user.serialize())


@app.route("/orders", methods=["GET"])
def get_orders():
    orders = db.session.query(models.Order).all()
    return jsonify([order.serialize() for order in orders])


@app.route("/orders/<int:id>", methods=["GET"])
def get_order_by_id(id):
    order = db.session.query(models.Order).filter(models.Order.id == id).first()

    if order is None:
        abort(404)

    return jsonify(order.serialize())


@app.route("/offers", methods=["GET"])
def get_offers():
    offers = db.session.query(models.Offer).all()
    return jsonify([offer.serialize() for offer in offers])


@app.route("/offers/<int:id>", methods=["GET"])
def get_offer_by_id(id):
    offer = db.session.query(models.Offer).filter(models.Offer.id == id).first()

    if offer is None:
        abort(404)

    return jsonify(offer.serialize())


# обработка данных от клиента
@app.route("/users", methods=["POST"])
def create_user():
    content = request.json

    with db.session.begin():
        db.session.add(models.User(**content))

    return {"message": 'User add success!'}


@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    content = request.json
    with db.session.begin():
        if db.session.query(models.User).filter(models.User.id == id).first() is None:
            abort(404)
        db.session.query(models.User).filter(models.User.id == id).update(content)

    return {"message": 'User update success!'}


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user():
    with db.session.begin():
        if db.session.query(models.User).filter(models.User.id == id).first() is None:
            abort(404)
        db.session.query(models.User).filter(models.User.id == id).delete()

    return {"message": 'User DELETE success!'}


@app.route("/orders", methods=["POST"])
def create_order():
    content = request.json
    with db.session.begin():
        db.session.add(models.Order(**content))

    return {"message": 'order add success!'}


@app.route("/orders/<int:id>", methods=["PUT"])
def update_order(id):
    content = validate_json(request.json)

    with db.session.begin():
        if db.session.query(models.Order).filter(models.Order.id == id).first() is None:
            abort(404)
        db.session.query(models.Order).filter(models.Order.id == id).update(content)

    return {"message": 'order update success!'}


@app.route("/orders/<int:id>", methods=["DELETE"])
def delete_order(id):
    with db.session.begin():
        if db.session.query(models.Order).filter(models.Order.id == id).first() is None:
            abort(404)
        db.session.query(models.Order).filter(models.Order.id == id).delete()

    return {"message": 'order DELETE success!'}


@app.route("/offers", methods=["POST"])
def create_offer():
    content = request.json
    with db.session.begin():
        db.session.add(models.Offer(**content))

    return {"message": 'offer add success!'}


@app.route("/offers/<int:id>", methods=["PUT"])
def update_offer(id):
    content = validate_json(request.json)
    with db.session.begin():
        if db.session.query(models.Offer).filter(models.Offer.id == id).first() is None:
            abort(404)
        db.session.query(models.Offer).filter(models.Offer.id == id).update(content)

    return {"message": 'offer update success!'}


@app.route("/offers/<int:id>", methods=["DELETE"])
def delete_offer(id):
    with db.session.begin():
        if db.session.query(models.Offer).filter(models.Offer.id == id).first() is None:
            abort(404)
        db.session.query(models.Offer).filter(models.Offer.id == id).delete()

    return {"message": 'offer DELETE success!'}
