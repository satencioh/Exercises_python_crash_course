def describe_mascota(tipo_animal, nombre_mascota):
    """Mostrar informacion de una mascoyta"""
    print(f"\nYo tengo un {tipo_animal.title()}")
    print(f"El nombre de mi {tipo_animal.title()} es {nombre_mascota.title()}")

describe_mascota('gato', 'gala')