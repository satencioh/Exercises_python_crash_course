favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward':'ruby',
    'phill':'python',
}
#iterar sobre la llave y valor de un diccionario dinamicamente
# for k, v in favorite_languages.items():
#     print(f"\nel lenguaje favorito de {k.title()} es {v.title()}.")

#iterar sobre las llaves de un diccionario dinamicamente
# for nombre in favorite_languages.keys():
#     print(nombre.title())

for lenguaje in favorite_languages.values():
    print(lenguaje.title())