import json
from datetime import datetime as dt
from typing import Dict, List


customers = []
file_path = ''

class Customer:
    def __init__(self, id, name, vat_id, email, phone):
        self.id = id
        self.name = name
        self.vat_id = vat_id
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'({self.id})\t{self.name}'



def save_customer(data):
    print('save() is working')

def get_all_customers() -> List[Customer]:
    return customers

def get_customer(id: int) -> Customer:
    return customers[id - 1]

def update_customer(data):
    print('update() is working')

def delete_customer(id):
    print('delete() is working')

# privatna metoda koja rjecnik pretvori u objekt klase Customer
def dict_to_customer(dictionary):
    return Customer(dictionary['id'],
                    dictionary['name'],
                    dictionary['vat_id'],
                    dictionary['email'],
                    dictionary['phone'])

# privatna metoda koja objekt klase Customer pretvori u rjecnik
def customer_to_dict():
    pass

def load_data(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_reader:
            # Ocisti listu od starih podataka prije ucitavanja
            customers.clear()
            # ucitamo listu rjecnika i konvertiramo ih u listu objekata klase Customer
            data = json.load(file_reader)
            for element in data:
                customer = dict_to_customer(element)
                customers.append(customer)
            return customers
    except Exception as ex:
        print(f'{dt.now()} - Dogodila se greska {ex}!')
        return []


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
    # Ovo moram napraviti jer mijenjam
    # varijablu unutar funkcije
    global customers
    # ucitamo postavke aplikacije u rjecnik
    app_config = app_init()
    # Prije nastavka ucitam sve podatke u listu
    customers = load_data(app_config['file_path'])

    # provjerimo je li bilo gresaka, odnosno ima li podataka pod kljucem error_message
    if app_config['error_message'] != '':
        print(app_config['error_message'])
        # sys.exit()
        return

    # CRUD (Create, Read ili Retreive, Update, Delete) metode repozitorija
    # repo.save([])
    all_customers = get_all_customers()
    for customer in all_customers:
        print(customer)
    print()
    customer_5 = get_customer(25)
    print(customer_5.phone)
    # repo.update([])
    # repo.delete(13)


if __name__ == '__main__':
    main()
