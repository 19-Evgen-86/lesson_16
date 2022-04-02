from orders import orders
from flask import request, abort, jsonify
from app import db, models, utils


@orders.route("/get/all/", methods=["GET"])
def get_orders():
    orders = db.session.query(models.Order).all()
    return jsonify([order.serialize() for order in orders])


@orders.route("/get/<int:id>", methods=["GET"])
def get_order_by_id(id):
    order = db.session.query(models.Order).filter(models.Order.id == id).first()

    if order is None:
        abort(404)

    return jsonify(order.serialize())

@orders.route("/new/", methods=["POST"])
def create_order():
    content = request.json
    with db.session.begin():
        db.session.add(models.Order(**content))

    return {"message": 'Order add success!'}


@orders.route("/update/<int:id>", methods=["PUT"])
def update_order(id):
    content = utils.validate_json(request.json)
    with db.session.begin():
        if db.session.query(models.Order).filter(models.Order.id == id).first() is None:
            abort(404)
        db.session.query(models.Order).filter(models.Order.id == id).update(content)

    return {"message": 'Order update success!'}


@orders.route("/delete/<int:id>", methods=["DELETE"])
def delete_order(id):
    with db.session.begin():
        if db.session.query(models.Order).filter(models.Order.id == id).first() is None:
            abort(404)
        db.session.query(models.Order).filter(models.Order.id == id).delete()

    return {"message": 'Order DELETE success!'}
