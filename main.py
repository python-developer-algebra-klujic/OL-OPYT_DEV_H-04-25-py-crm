import json
from datetime import datetime as dt
import sys
from typing import Dict


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


# Funkcija koja inicijalizira pocetne postavke nase aplikacije
def app_init() -> Dict:
    try:
        with open('./data_store/settings.json') as file_reader:
            # ako sve dobro prode onda ce vratiti rjecnik s postavkama
            return json.load(file_reader)
    except Exception as ex:
        # ako se dogodi greska onda ce vratiti rjecnik s error porukom
        return {
            'error_message': f'{dt.now()} - {ex}'
        }


# Glavna funkcija iz koje se pokrece aplikacija
def main():
    # ucitamo postavke aplikacije u rjecnik
    app_config = app_init()

    # provjerimo je li bilo gresaka, odnosno ima li podataka pod kljucem error_message
    if app_config['error_message'] != '':
        print(app_config['error_message'])
        # sys.exit()
        return
    else:
        repo = Repository(app_config['file_path'])

    # CRUD (Create, Read ili Retreive, Update, Delete) metode repozitorija
    repo.save([])
    repo.get_all()
    repo.get(5)
    repo.update([])
    repo.delete(13)


if __name__ == '__main__':
    main()
