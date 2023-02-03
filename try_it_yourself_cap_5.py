# car = 'subaru'

# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# almacen = ['televisor','lavadora','estufa','nevera']
# producto = 'nevera'

# if producto == 'computador':
#     print(f'el producto efectivamente es {producto}')

# if producto.lower() == 'nevera':
#     print(f'el producto es diferente')

#ejercicio 5-2
# alien_color = 'red'

# if 'green' in alien_color:
#     puntos = 5
# print(f"haz ganado {puntos} puntos")


# if 'blue' in alien_color:
#     print("haz ganado 5 puntos")

# if 'green' in alien_color:
#     print("haz ganado 5 puntos por dispararle al alien")
# else:
#     print("haz ganado 10 puntos")

# if 'blue' in alien_color:
#     print("haz ganado 5 puntos por dispararle al alien")
# else:
#     print("haz ganado 10 puntos")

# if alien_color == 'blue':
#     print("haz ganado 5 puntos por dispararle al alien")
# elif alien_color == 'yelow':
#     print("haz ganado 10 puntos por dispararle al alien")
# else:
#     print("haz ganado 15 puntos por dispararle al alien")

# age = 17

# if age < 2:
#     print("la perona es un bebe")
# elif age < 4:
#     print("la persona es un niño pequeño")
# elif age < 13:
#     print("la persona es un niño")
# elif age < 20:
#     print("la persona es un adolecente")
# elif age < 65:
#     print("la persona es un adulto")
# else:
#     print("la persona es mayor")

# frutas_fav = ['mango','coco','manzana']

# if 'mango' in frutas_fav:
#     print("te gusta mucho el mango")
# if 'banana' in frutas_fav:
#     print("te gusta mucho las bananas")
# if 'pera' in frutas_fav:
#     print("te gusta mucho la pera")
# if 'uva' in frutas_fav:
#     print("te gustan mucho las uvas")
# if 'manzana' in frutas_fav:
#     print("te gusta mucho la manzana")

# ejercicio 5-8
# users = ['sHernandez','lopezm','mr.robot','thanos','elpeligro','admin']

# for user in users:
#     if user == 'admin':
#         print(f"Hola {user} te gustaria ver un informe de estado?")
#     else:
#         print(f"Hola {user} gracias por loguearte nuevamente")

# ejercicio 5-9
# users = ['sofia24','lopezm','mr.robot','thanos','elpeligro','admin']
# users = []
# if users:
#     for user in users:
#         if user == 'admin':
#             print(f"Hola {user} te gustaria ver un informe de estado?")
#         else:
#             print(f"Hola {user} gracias por loguearte nuevamente")
# else:
#     print("Necesitamos en contrar algunos usuarios")

# ejercicio 5-10

# current_users = ['sHernandez','lopezm','mr.robot','thanos','elpeligro']
# new_users = ['sofia24','tuco','LALO','jessy','lopezm']

# current_users_lower =[]

# for current_user in current_users:
#      current_users_lower.append(current_user.lower())

# for user in new_users:
#     if user.lower() in current_users_lower:
#         print(f"el usuario {user} ya existe, ingrese un nuevo usuario")
#     else:
#         print(f"el usuario {user} esta disponible")

#ejercicio 5-11

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")