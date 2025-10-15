import json
from datetime import datetime as dt


class Repository:
    def __init__(self):
        pass

    def save(self, data):
        print('save() is working')

    def get_all(self):
        try:
            with open('./data_store/customers.json', 'r', encoding='utf-8') as file_reader:
                return json.load(file_reader)
        except Exception as ex:
            print(f'{dt.now()} - Dogodila se greska {ex}!')
            return []

    def get(self, id):
        print('get() is working')

    def update(self, data):
        print('update() is working')

    def delete(self, id):
        print('delete() is working')


def main():
    repo = Repository()

    repo.save([])
    repo.get_all()
    repo.get(5)
    repo.update([])
    repo.delete(13)


if __name__ == '__main__':
    main()
