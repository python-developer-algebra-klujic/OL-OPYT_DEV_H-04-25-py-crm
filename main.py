import json
from datetime import datetime as dt


try:
    with open('./data_store/customers.json', 'r', encoding='utf-8') as file_reader:
        data = json.load(file_reader)

        for dictionary in data:
            print(dictionary['name'])
except Exception as ex:
    print(f'{dt.now()} - Dogodila se greska {ex}!')
