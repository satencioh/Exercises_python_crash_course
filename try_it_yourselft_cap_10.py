# ejercicio 10-1
archivo = 'about_python.txt'

# print("--- leer archivo completo ---")
# with open(archivo) as ar:
#     linea = ar.read()
# print(linea)

# print("--- leer sobre cada linea ---")
# with open(archivo) as f:
#     for line in f:
#         print(line.rstrip())

# print("--- almacenar cada linea en lista ---")
# with open(archivo) as f:
#     line = f.readlines()

# for l in line:
#     print(l.rstrip())

#ejercicio 10-2

# print("--- reemplazando palabras ---")
# with open(archivo) as ar:
#     linea = ar.read()
#     linea_replace = linea.replace('Python', 'C')
# print(linea_replace)

#ejercicio 10-3

# nombre = input("Por favor ingresa tu nombre: ")
# archivo = 'invitados.txt'

# with open(archivo, 'a') as file:
#     file.write(nombre)

#ejercicio 10-4
# archivo = 'libro_invitados.txt'

# solicitud = True

# while solicitud:
#     nombre = input("Por favor ingresa tu nombre: ")

#     with open(archivo, 'a') as file:
#         file.write(f"{nombre}\n")

#     print(f"{nombre.title()} haz visitado nuestro lugar")

#     repeticion = input("Te gustaria dejar que otra persona responda? (y / n) ")
#     if repeticion == 'n':
#         solicitud = False

#ejercicio 10-6, 10-7

# while True:
#     num_1 = input("\nPrimer numero(para salir oprima (s) ): ")
#     if num_1 == 's':
#         break

#     num_2 = input("\nSegundo numero(para salir oprima (s) ): ")
#     if num_2 == 's':
#         break
#     try:
#     si lo que hay dentro del bloque try trabaja python salta el bloque de la except
#         resp = int(num_1) + int(num_2)
#     except ValueError:
#     si lo que esta dentro del bloque try no es exitoso python busca un bloque de excep cuyo error coincida con el que se genero
#         print("ha ingresado un tipo de dato string en alguno de sus numeros")
#     else:
#     esto se ejecutara solo si lo que esta dentro de try se ejeuto exitosamente
#         print(resp)

#ejercicio 10-8, 10-9

# filenames = ['cats.txt', 'dogs.txt', 'cows.txt']

# for file in filenames:
#     try:
#         with open(file) as f:
#             contents = f.read()
#             #print(contents)
#     except FileNotFoundError:
#         #print(f"Lo sentimos el archivo {file} no existe")
#         pass
#     else:
#         print(contents)

#ejercicio 10-10
# from word_count import count_words

# filenames = ['alice.txt', 'siddhartha.txt', 'micky_mouse.txt', 'moby_dick.txt', 'little_women.txt']
# for file in filenames:
#     count_words(file, 'the')


#ejercicio 10-12

import json

filename = 'favorite_num.json'

try:
    with open(filename) as f:
       number = json.load(f)
except FileNotFoundError:
    number = input("ingresa por favor tu numero favorito: ")
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(f"Tu numero favorito es: {number}")

