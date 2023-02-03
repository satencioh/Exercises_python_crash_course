import json

number = input("ingresa por favor tu numero favorito: ")
filename = 'favorite_num.json'

with open(filename, 'w') as f:
    json.dump(number, f)