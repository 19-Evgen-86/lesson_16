import datetime
import json
from os.path import isfile

from app import db


class Migrate:
    """
    Класс для миграции данный из json в БД
    """

    def __init__(self, file_path, model):
        # модель данных(для ORM)
        self.model = model
        # путь к файлу json с данными
        self.file_path = file_path

    def load_json(self):
        """
        Загружает данные из JSON
        :return: список с данными
        """
        data = []
        if isfile(self.file_path):
            with open(self.file_path, encoding="utf-8") as file:
                data = json.load(file)
        return data

    def insert_to_base(self):
        """
        Добавляет данные в БД
        :return:
        """
        data = self.validate(self.load_json())
        with db.session.begin():
            for item in data:
                if db.session.query(self.model).filter(self.model.id == item["id"]).first() is None:
                    item_base = self.model(**item)
                    db.session.add(item_base)

    def validate(self, json_data):
        """
        Проверяет данные, приводит в соответствие со структурой БД.
        :param json_data:
        :return: Валидный список данных
        """
        validate_result = []
        for items in json_data:
            for key, value in items.items():
                if isinstance(value, str) and value.count('/') == 2:
                    items[key] = datetime.datetime.strptime(value, "%m/%d/%Y")
            validate_result.append(items)
        return validate_result


def validate_json(json_data):
    """
    Проверяет данные, приводит в соответствие со структурой БД.
    :param json_data (полученный json от клиента)
    :return: Валидные данные
    """

    for key, value in json_data.items():
        if isinstance(value, str) and value.count('/') == 2:
            json_data[key] = datetime.datetime.strptime(value, "%m/%d/%Y")

    return json_data
