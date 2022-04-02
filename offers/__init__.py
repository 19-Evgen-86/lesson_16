from flask import Blueprint

offers = Blueprint('offers', __name__)

from offers import route
