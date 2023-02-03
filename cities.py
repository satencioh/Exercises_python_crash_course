prompt = "\nIngrese el nombre de la ciudad que haz visitado: "
prompt += "\nIngresar 'quit' para finalizar el programa "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Me gustaria ir a {city.title()}")