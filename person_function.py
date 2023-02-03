# def construir_persona(nombre, apellido, edad=None):
#     persona = {'nombre': nombre, 'apellido':apellido}
#     if edad:
#         persona['edad'] = edad
#     return persona

# musician = construir_persona('Sofia', 'Vergara', 26)
# print(musician)

# musician = construir_persona('Pedro', 'Fernandez')
# print(musician)

def construir_persona(nombre, apellido):
    persona = f"{nombre} {apellido}"
    return persona.title()

while True:
    print("\nDime tu nombre: ")
    print("(ingres 'q' para salir)")

    f_name = input("nombre: ")
    if f_name == 'q':
        break
    l_name = input("apellido: ")
    if l_name == 'q':
        break


musico = construir_persona(f_name, l_name)
print(f"\nHola, {musico}")