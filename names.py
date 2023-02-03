from name_function import get_formatted_name

print("ingrese 's' para salir")
while True:
    first = input("Ingresa tu nombre: ")
    if first == 's':
        break
    last = input("Ingrese su apellido: ")
    if last == 's':
        break

    formatted = get_formatted_name(first, last)
    print(f"\tNombre completamente formateado: {formatted}.")