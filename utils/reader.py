import csv
import json

def read_users_csv():
    with open("data/users.csv",newline="") as file:
        reader = csv.DictReader(file)   
        return list(reader)

def read_productos_json():
    with open("data/products.json", encoding="utf-8") as file: #El encoding es para que no de error con los acentos
        return json.load(file)
    
data = read_users_csv()
print(data[0])

        
        