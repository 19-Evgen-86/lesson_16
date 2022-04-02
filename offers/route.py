from offers import offers
from flask import jsonify, abort, request
from app import db, models, utils


@offers.route("/get/all/", methods=["GET"])
def get_offers():
    offers = db.session.query(models.Offer).all()
    return jsonify([offer.serialize() for offer in offers])


@offers.route("/get/<int:id>", methods=["GET"])
def get_offer_by_id(id):
    offer = db.session.query(models.Offer).filter(models.Offer.id == id).first()

    if offer is None:
        abort(404)

    return jsonify(offer.serialize())


@offers.route("/new/", methods=["POST"])
def create_offer():
    content = request.json
    with db.session.begin():
        db.session.add(models.Offer(**content))

    return {"message": 'offer add success!'}


@offers.route("/update/<int:id>", methods=["PUT"])
def update_offer(id):
    content = utils.validate_json(request.json)
    with db.session.begin():
        if db.session.query(models.Offer).filter(models.Offer.id == id).first() is None:
            abort(404)
        db.session.query(models.Offer).filter(models.Offer.id == id).update(content)

    return {"message": 'offer update success!'}


@offers.route("/delete/<int:id>", methods=["DELETE"])
def delete_offer(id):
    with db.session.begin():
        if db.session.query(models.Offer).filter(models.Offer.id == id).first() is None:
            abort(404)
        db.session.query(models.Offer).filter(models.Offer.id == id).delete()

    return {"message": 'offer DELETE success!'}
