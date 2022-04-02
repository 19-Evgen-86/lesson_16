from flask import Blueprint

orders = Blueprint('orders', __name__)
from orders import route