'''
... stari zahtjevi
Novi zahtjev - dodati podatke o djelatnicima firme koja koristi CRM aplikaciju
Djelatnik se treba prijaviti u aplikaciju. podaci se cuvaju u datoteci employees.json
u kojoj mora biti prvi djelatnik Administrator s:
    username - Admin
    password - Pass4Admin
'''

import json
from datetime import datetime as dt
from typing import Dict, List

#region EMPLOYEE
# klasa koja cuva podatke o djelatniku firme koja koristi ovu nasu aplikaciju
class Employee:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 username: str,
                 password: str,
                 job_description: str,
                 format_full_name: str = 'FL', # FL - Prikazi prvo First name pa Last name
                 is_admin: bool = False):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.job_description = job_description
        self.is_admin = is_admin
        self.format_full_name = format_full_name
        self.full_name = self._construct_full_name()

    def __str__(self):
        return f'{self.full_name}'

    def _construct_full_name(self):
        if self.format_full_name == 'FL':
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.last_name} {self.first_name}'

class EmployeeRepository:
    def __init__(self, file_path):
        pass

    def _load_data(self, file_path: str):
        pass

    def save(self, employee: Employee):
        pass

    def get_by_username(self, username: str) -> Employee:
        pass

    def get_by_id(self, id: int) -> Employee:
        pass


# Klasa koja upravlja prijavom i odjavom korisnika u aplikaciji
class AuthManager:
    def __init__(self):
        self.loggedin_user: Employee = None

    def login(self, username: str, password: str) -> str:
        """"username -> username ili email"""
        # generirati simulaciju tokena
        # Ako prode sve provjere dohvatiti iz liste
        user_from_db = self.repo.get_by_username(username)
        self.loggedin_user = user_from_db

    def logout(self, token: str):
        '''dodati algoritam'''
        pass

    def change_password(self, username: str, old_password: str, new_password: str):
        # provjera postojeceg passworda
        # user not found!!!
        '''
        ALGORITAM
        0. Preskociti provjere jesu li passwordi '' i nije bitna duzina passworda
        1. Provjera postoji li korisnik u bazi/employees.json koji ima isti username
            kao i onaj naveden u argumentima metode
        1.2. Ako ima -> provjeriti je li old_password OK
        1.2.1.  Ako je ispravan -> trazimo dodatni unos novog passworda
        1.2.1.1.    Ako je ispravan onda na objektu employee promjenimo pwd i pohranimo ga u store
        1.2.1.2.    Ako nije ispravan -> pokusaj ponovno ili odustani
        '''
        # Samo ADmin moze mijenjati passworde sebi i drugima
        if self.loggedin_user.is_admin:
            user_from_db = self.repo.get_by_username(username)
            if user_from_db != None:
                if user_from_db.password == old_password:
                    while True:
                        # Dodatni unos novog passworda
                        # Ako je OK promijeni
                        user_from_db.password = new_password
                        self.repo.save()
        else:
            return f'{self.loggedin_user.full_name}, nemate pravo mijenjati password!'


#endregion

#region CUSTOMER

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


class CustomerRepository:
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

#endregion

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
        repo = CustomerRepository(app_config['file_path'])
        users_repo = EmployeeRepository(app_config['file_path'])
        auth_manager = AuthManager(app_config['file_path'])


    app_loggedin_user = None
    if app_loggedin_user == None:
        username = input('Upisite vas username: ')
        password = input('Upisite vas password: ')
        user = users_repo.get_by_username(username)

        jwt_token = auth_manager.login(username, password)

    # CRUD (Create, Read ili Retreive, Update, Delete) metode repozitorija
    # repo.save([])
    all_customers = repo.get_all()
    for customer in all_customers:
        print(customer)
    print()
    customer_5 = repo.get(25)
    print(customer_5.phone)
    print(customer_5.full_name)
    print()
    employee = Employee('Pero', 'Peric', 'pperic', 'Pa$$w0rd!', 'CEO', 'FL', True)
    print(employee)
    # repo.update([])
    # repo.delete(13)


if __name__ == '__main__':
    main()
