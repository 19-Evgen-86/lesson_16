from users import users
from flask import request, abort, jsonify
from app import db, models, utils


@users.route("/get/all/", methods=["GET"])
def get_users():
    users = db.session.query(models.User).all()
    return jsonify([user.serialize() for user in users])


@users.route("/get/<int:id>", methods=["GET"])
def get_order_by_id(id):
    user = db.session.query(models.User).filter(models.User.id == id).first()

    if user is None:
        abort(404)

    return jsonify(user.serialize())


@users.route("/new/", methods=["POST"])
def create_order():
    content = request.json
    with db.session.begin():
        db.session.add(models.User(**content))

    return {"message": 'User add success!'}


@users.route("/update/<int:id>", methods=["PUT"])
def update_order(id):
    content = utils.validate_json(request.json)
    with db.session.begin():
        if db.session.query(models.User).filter(models.User.id == id).first() is None:
            abort(404)
        db.session.query(models.User).filter(models.User.id == id).update(content)

    return {"message": 'User update success!'}


@users.route("/delete/<int:id>", methods=["DELETE"])
def delete_order(id):
    with db.session.begin():
        if db.session.query(models.User).filter(models.User.id == id).first() is None:
            abort(404)
        db.session.query(models.User).filter(models.User.id == id).delete()

    return {"message": 'User DELETE success!'}
