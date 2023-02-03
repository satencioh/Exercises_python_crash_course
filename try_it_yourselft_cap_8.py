# ejercicio 8-1, 8-2
# def libro_favorito(titulo):
#     print(f"Uno de mis libros favoritos es {titulo.title()}")

# libro_favorito('indomable')

#ejercicio 8-3, 8-4
# def hacer_camisa(talla, texto):
#     print(f"El tamaño de la camisa es {talla.title()}, y el mensaje a imprimir es {texto}")

#hacer_camisa('l', 'I love AWS')
#hacer_camisa(talla='m', texto='La vida es linda')
# hacer_camisa('grande', 'I love Python')
# hacer_camisa(texto='el mundo increible', talla='mediana')

#8-5
# def describir_ciudad(ciudad, pais='francia'):
#     print(f"{ciudad.title()} esta en {pais.title()}")

# describir_ciudad('paris')
# describir_ciudad('londres')
# describir_ciudad('Toronto', 'Canada')

#8-6
# def ciudad_pais(ciudad, pais):
#     return f"{ciudad.title()}, {pais.title()}"

# info = ciudad_pais('santiago', 'chile')
# print(info)
# info = ciudad_pais('bogota', 'colombia')
# print(info)
# info = ciudad_pais('madrid', 'españa')
# print(info)

#8-7

# def hacer_album(artista, album, pista=None):
#     """contruir un album musical"""
#     album_info = {'artista': artista.title(), 'album':album.title()}
#     if pista:
#         album_info['No. pista'] = pista
#     return album_info

# while True:
#     print("(ingres 's' para salir)")

#     info_artista = input("Nombre de artista: ")
#     if info_artista == 's':
#         break

#     info_album = input("Nombre de album: ")
#     if info_artista == 's':
#         break

#     info_pista = input("numero de pistas: ")
#     if info_pista == 's':
#         break
    
#     albumnes = hacer_album(info_artista, info_album, info_pista)
#     print(albumnes)

# ejercicio 8-9
# def mostrar_msj(mensajes_texto):
#     for msj in mensajes_texto:
#         print(f"Mensaje #: {mensajes_texto.index(msj)} => {msj}")

# mensajes_texto = ['Hola mundo','Le habla el Banco para dar informacion sobre productos','Ya esta tu mercado listo, puedes pasar por el']

# mostrar_msj(mensajes_texto)

# def imprimir_msj(mensajes_sin_env):
#     print("Mostrando mensajes.....")
#     for msj in mensajes_sin_env:
#         print(msj)

# def enviar_msj(mensajes_sin_env, mensaje_enviado):
#     print("enviando mensaje.....")
#     while mensajes_sin_env:
#         enviando_msj = mensajes_sin_env.pop()
#         print(enviando_msj)
#         mensaje_enviado.append(enviando_msj)

# mensajes_sin_env = ['Hola mundo','Le habla el Banco para dar informacion sobre productos','Ya esta tu mercado listo, puedes pasar por el']
# mensaje_enviado = []

# imprimir_msj(mensajes_sin_env)
# enviar_msj(mensajes_sin_env, mensaje_enviado)

#enviar_msj(mensajes_sin_env[:], mensaje_enviado)
# print("\nLista final..")
# print(mensajes_sin_env)
# print(mensaje_enviado)


# ejercicio 8-12
# def items(*items):
#     print("\nEstos son los items que quieres en tu sandwich: ")
#     for item in items:
#         print(f"-{item.title()}")

# #items('queso','bbq','cebolla','kabano')
# #items('salchicha','tartara')
# items('champiñon','piña','queso','tomate','lechuga','salsa mexicana')

#ejercicio 8-13
# def contruir_perfil(nombre, apellido, **info_adicional):
#     info_adicional['nombre'] = nombre
#     info_adicional['apellido'] = apellido
#     return info_adicional

# perfil_usuario = contruir_perfil('Luisa', 'Hernandez', 
#                                     ubicacion='codazzi', 
#                                     profesion='cientifico de datos',
#                                     deporte='balonsexto',
#                                     lugar_fav='Europa')

# print(perfil_usuario)

# ejercicio 8-14
# def info_carro(fabricante, modelo, **info_adicional):
#     info_adicional['Fabricante'] = fabricante.title()
#     info_adicional['Modelo'] = modelo.title()
#     return info_adicional

# carro = info_carro('bmw','bmw X7',
#                     color='rojo',
#                     motor='ultima Gen',
#                     blindado=True)

# print(carro)

#ejercicio 8-15
# import print_model

# diseño_sinimp =['casa arquitectonica','zapato ortopedico', 'gafas medicas']
# modelo_completado = []

# print_model.imprimir_modelo(diseño_sinimp, modelo_completado)
# print_model.mostrar_modelos(modelo_completado)

#ejercicio 8-16
import print_model # importa el modulo
from print_model import mostrar_modelos # importa una funcion del modulo
from print_model import imprimir_modelo as im # importa una funcion del modulo y le asigna un alias
import print_model as pm # importa un modulo asignandole un alias
from print_model import * # importa todas las funciones del modulo
