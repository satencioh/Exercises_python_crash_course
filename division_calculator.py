# try:
# # si lo que hay dentro del bloque try trabaja python salta el bloque de la except
#     print(5/0)
# except ZeroDivisionError:
# # de lo contrario python busca un bloque de excep cuyo error coincida con el que se genero
#     print("no puedes dividir por cero")

while True:
    num_1 = input("\nPrimer numero(para salir oprima (s) ): ")
    if num_1 == 's':
        break

    num_2 = input("\nSegundo numero(para salir oprima (s) ): ")
    if num_2 == 's':
        break
    try:
    # si lo que hay dentro del bloque try trabaja python salta el bloque de la except
        resp = int(num_1) / int(num_2)
    except ZeroDivisionError:
    # si lo que esta dentro del bloque try no es exitoso python busca un bloque de excep cuyo error coincida con el que se genero
        print("no puedes dividir por cero")
    else:
    # esto se ejecutara solo si lo que esta dentro de try se ejeuto exitosamente
        print(resp)