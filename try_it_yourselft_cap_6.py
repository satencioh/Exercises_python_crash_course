#ejercicio 6-1
# persona = {'nombre': 'Luis', 'edad': 27, 'ciudad':'santa marta'}

# print(f"la persona {persona['nombre'].title()} tiene {persona['edad']} años y vive en la ciudad de {persona['ciudad'].title()}")

#ejercicio 6-2
# favorite_numbers = {'Luis':8, 'sofia':20, 'pedro':2, 'gala': 96, 'catty': 54}

# for persona in favorite_numbers:
#     print(f'el numero favorito de {persona} es {favorite_numbers.get(persona)}')

#ejercicio 6-3

# glosario = {
#     'variable':'donde se almacena el valor de un objeto', 
#     'lista':'es una estrutrua de datos dinamica que contiene una coleccion de elementos', 
#     'tuplas':'es una estrutrua de datos estatica que contiene una coleccion de elementos',
#     'diccionario':'coleccion de pares llave-valor'
# }

# for item in glosario:
#     print(f'\n{item} = {glosario.get(item)}')

#ejercicio 6-4
# glosario = {
#     'variable':'donde se almacena el valor de un objeto', 
#     'lista':'es una estrutrua de datos dinamica que contiene una coleccion de elementos', 
#     'tuplas':'es una estrutrua de datos estatica que contiene una coleccion de elementos',
#     'diccionario':'coleccion de pares llave-valor',
#     'llave': 'El primer elemento de un par clave-valor en un diccionario',
#     'valor':'un item asociado con una llave en un diccionario',
#     'expresion booleana': 'expresion que evalua verdadero o falso'
# }

# for item in glosario:
#     print(f'\n{item} = {glosario.get(item)}')

#ejercicio 6-5
# rios ={
#     'río volga':'rusia',
#     'río li':'china',
#     'caño cristales':'colombia'
# }

# for k, v in rios.items():
#     print(f"\nEl {k.title()} atraviesa {v.title()} ")

# for k in rios:
#     print(f"\n{k.title()} ")

# for v in rios.values():
#     print(f"\n{v.title()} ")

#ejercicio 6-6

# favorite_languages = {
#     'jen':'python',
#     'sarah': 'c',
#     'edward':'ruby',
#     'phill':'python',
# }

# poll = ['luis','carolina','catty','jen','phill']
#iterar sobre la llave y valor de un diccionario dinamicamente
# for k, v in favorite_languages.items():
#     print(f"\nel lenguaje favorito de {k.title()} es {v.title()}.")

#iterar sobre las llaves de un diccionario dinamicamente
# for nombre in favorite_languages.keys():
#     print(nombre.title())

# for lenguaje in favorite_languages.values():
#     print(lenguaje.title())

# for persona in poll:
#     if not persona in favorite_languages:
#         print(f"{persona.title()} debes tomar la encuesta")
#     else:
#         print(f"{persona.title()} gracias por responder la encuesta")

#ejercicio 6-7
# persona_0 = {'nombre': 'carolina', 'edad': 27, 'ciudad':'barranquilla'}
# persona_1 = {'nombre': 'luis', 'edad': 26, 'ciudad':'bucaramanga'}
# persona_2 = {'nombre': 'alfonso', 'edad': 15, 'ciudad':'bogota'}

# personas = [persona_0, persona_1, persona_2]

# for persona in personas:
#     print(f"la persona {persona['nombre'].title()} tiene {persona['edad']} años y vive en la ciudad de {persona['ciudad'].title()}")

#ejercicio 6-9

# lugares_fav = {
#     'luis': 'ontario',
#     'sofia': 'londres',
#     'catty': 'mishilandia'
# }

# for p, l in lugares_fav.items():
#     print(f"\nEl lugar favorito de {p.title()} es {l.title()}")

#ejercicio 6-10
favorite_numbers = {
    'luis':[8,58,1], 
    'sofia':[20,7,3],
    'pedro':[2,88],
    'gala':[5,51,96], 
    'catty': [54,22]
}

for p, n in favorite_numbers.items():
    print(f'los numeros favoritos de {p.title()} son:')
    for number in n:
        print(f"\t{number}")