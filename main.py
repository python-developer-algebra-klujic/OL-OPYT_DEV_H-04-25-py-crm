import json
from datetime import datetime as dt


class Repository:
    def __init__(self):
        pass

    def save(self, data):
        pass

    def get_all():
        pass

    def get(self, id):
        pass

    def update(self, data):
        pass

    def delete(self, id):
        pass






try:
    with open('./data_store/customers.json', 'r', encoding='utf-8') as file_reader:
        data = json.load(file_reader)

        for dictionary in data:
            print(dictionary['name'])
except Exception as ex:
    print(f'{dt.now()} - Dogodila se greska {ex}!')


repo = Repository()

repo.save(data)
repo.get_all()
repo.get(5)
repo.update(data)
repo.delete(13)
