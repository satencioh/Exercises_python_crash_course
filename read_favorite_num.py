import json

filename = 'favorite_num.json'

with open(filename) as f:
    contents = json.load(f)
print(f"Yo se que tu numero favorito es: {contents}")