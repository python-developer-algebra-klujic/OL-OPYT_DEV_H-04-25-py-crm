import json
from datetime import datetime as dt
from typing import Dict, List


class Customer:
    def __init__(self, id, name, vat_id, email, phone):
        self.id = id
        self.name: str = name
        self.vat_id = vat_id
        self.email = email
        self.phone = phone
        self.full_name: str = self._get_full_name()

    def __str__(self):
        return f'({self.id})\t{self.name}'

    def _get_full_name(self):
        return f'Puno ime: {self.name.capitalize()}'


class Repository:
    def __init__(self, file_path: str):
        # private property - sugerira da je samo za primjenu unutar klase
        self._file_path = file_path
        # kod kreiranja objekta ucitaju se svi podaci i napuni se ovo svojstvo
        self._customers = []
        self._load_data()

    def save(self, data):
        print('save() is working')

    def get_all(self) -> List[Customer]:
        return self._customers

    def get(self, id: int) -> Customer:
        return self._customers[id - 1]

    def update(self, data):
        print('update() is working')

    def delete(self, id):
        print('delete() is working')

    # privatna metoda koja rjecnik pretvori u objekt klase Customer
    def _dict_to_customer(self, dictionary):
        return Customer(dictionary['id'],
                        dictionary['name'],
                        dictionary['vat_id'],
                        dictionary['email'],
                        dictionary['phone'])

    # privatna metoda koja objekt klase Customer pretvori u rjecnik
    def _customer_to_dict(self):
        pass

    def _load_data(self):
        try:
            with open(self._file_path, 'r', encoding='utf-8') as file_reader:
                self._customers.clear()
                # ucitamo listu rjecnika i konvertiramo ih u listu objekata klase Customer
                data = json.load(file_reader)
                for element in data:
                    customer = self._dict_to_customer(element)
                    self._customers.append(customer)
        except Exception as ex:
            print(f'{dt.now()} - Dogodila se greska {ex}!')
            self._customers = []


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
    # repo.save([])
    all_customers = repo.get_all()
    for customer in all_customers:
        print(customer)
    print()
    customer_5 = repo.get(25)
    print(customer_5.phone)
    print(customer_5.full_name)
    # repo.update([])
    # repo.delete(13)


if __name__ == '__main__':
    main()
