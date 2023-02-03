#ejercicio 7-1
# car = input("que tipo de carro te gustaria rentar? ")

# print(f"Permiteme ver si puedo encontrar un {car.title()}")

#ejercicio 7-2
# cantidad_personas = input("Cuantas personas hay en su grupo de cena? ")

# cantidad_personas = int(cantidad_personas)

# if cantidad_personas > 8:
#     print("Ellos tendran que esperar para una mesa")
# else:
#     print("Su mesa esta lista")

#ejercicio 7-3
# numero = input("Ingrese un numero: ")
# numero = int(numero)

# if numero % 10 == 0:
#     print(f"el numero {numero} es multiplo de 10")
# else:
#     print(f"el numero {numero} no es multiplo de 10")

#ejercicio  7-4

# prompt = "\nIngresa una serie de ingredientes para pizza: "
# prompt +="\nSi deseas salir del programa ingresa 'salir'\n"

# ingrediente = ""

# while ingrediente != 'salir':
#     ingrediente = input(prompt)
#     if ingrediente == 'salir':
#         break
#     print(f"Haz agredado el ingrediente {ingrediente.title()}")

#ejercicio 7-5
# prompt = "\nIngresa tu edad y te dire el valor de tu ticket: "
# prompt +="\nSi deseas salir del programa ingresa 'salir'\n"


# while True:
#     age = input(prompt)
    
#     if age == 'salir':
#         break
#     age = int(age)

#     if age < 3:
#         print("Su ticket es gratis")
#         break
#     elif age < 13:
#         print("Su ticket tiene el precio de $10")
#         break
#     else:
#         print("Su ticket tiene el precio de $15")
#         break

#ejercicio 7-8, 7-9
# sandwich_orders = ['mexicano', 'pastrami', 'crujiente', 'pastrami', 'metro','baguette', 'frescura', 'pastrami']
# finished_sandwich = []

# print("El local ya no dispone de Pastrami")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     sandwich_made = sandwich_orders.pop()

#     print(f"Estoy haciendo tu sandwich {sandwich_made.title()}")

#     finished_sandwich.append(sandwich_made)


# print("los siguientes sandwich se elaboraron: ")
# for s in finished_sandwich:
#     print(s.title())

respuestas = []
encuesta_activa = True

while encuesta_activa:
    respuesta = input("Si pudieras visitar un lugar en el mundo, donde te gustaria ir? ")

    respuestas.append(respuesta)

    repeticion = input("Te gustaria dejar que otra persona responda? (yes / no) ")
    if repeticion == 'no':
        encuesta_activa = False

print("Lugares que a los usurios les gustaria visitar: ")

for lugar in respuestas:
    print(lugar.title())