import os
from os.path import join

DATABASE_PATH = join(os.getcwd(), 'base.db')


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_DATA_PATH = join("json_files", "users.json")
    ORDER_DATA_PATH = join("json_files", "orders.json")
    OFFER_DATA_PATH = join("json_files", "offer.json")
    JSON_AS_ASCII = False
