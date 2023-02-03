import json
#1. si existe el filename, get_stored_username abrirar el archivo y cargara lo que hay en el
#guardandolo en la variable username, la cual es retornada
#2. la funcion get_new_username solicita un nuevo usuario en caso de que filename no existiera y retorna username
#3.luego la funcion greet_user valida si username es true (o tiene algo) es decir si filename existe imprime
#lo del if (la bienvenida) si no existe el filename, solicita el username y crear el filename ejecutando lo del else
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():

        username = input("Cual es tu nombre: ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
        return username

def greet_user():
    """Saludar al usuario por el nombre"""
    
    username = get_stored_username()
    if username:
        r = input(f"el usuario {username} es correcto (y/n): ")
        if r == 'y':
            print(f"Bienvenido de nuevo {username}")
        else:
            username = get_new_username()
            print(f"Nosotros te recordaremos cuando vuelvas {username} ")
    else:
        username = get_new_username()
        print(f"Nosotros te recordaremos cuando vuelvas {username} ")

greet_user()
