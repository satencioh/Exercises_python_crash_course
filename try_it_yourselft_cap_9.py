# ejercicio 9-1
# class Restaurant():
#     """clase para modelar un restaurante"""

#     def __init__(self, restaurant_name, cuisine_type):
#         self.nombre_restaurante = restaurant_name
#         self.tipo_cocina = cuisine_type

#     def describe_restaurant(self):
#         print(f"nombre del restaurante {self.nombre_restaurante}")
#         print(f"tipo de cocina {self.tipo_cocina}")
    
#     def open_restaurant(self):
#         print(f"el restaurante {self.nombre_restaurante} ya se encuentra abierto")


# restaurant_1 = Restaurant("Doña petrona", "Comida de mar")
# restaurant_2 = Restaurant("Señora Bucaramanga", "Comida tipica")
# restaurant_3 = Restaurant("Montacarga Valledupar", "Comida rapida")

# print(f"{restaurant_1.nombre_restaurante} ------ {restaurant_1.tipo_cocina}")
# restaurant_1.describe_restaurant()
# restaurant_1.open_restaurant()

# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()

# ejercicio 9-3
# class User():
#     """clase para modelar un usuario"""

#     def __init__(self, first_name, last_name, address, city, nickname):
#         self.nombre = first_name
#         self.apellido = last_name
#         self.direccion = address
#         self.ciudad = city
#         self.usuario = nickname

#     def describe_user(self):
#         """describe informacion del usuario"""
#         print("\n ----- datos de usuario ------ ")
#         print(f"Nombre ===> {self.nombre} ")
#         print(f"apellidos ===> {self.apellido} ")
#         print(f"direccion ===> {self.direccion} ")
#         print(f"ciudad ===> {self.ciudad} ")
#         print(f"usuario ===> {self.usuario} ")

#     def greet_user(self):
#         """metodo de saludo"""
#         print(f"\nHola {self.nombre} bienvenido a nuesto sitio web!!!")
        

# usuario_1 = User("Sofia", "Lopez","cra 55 #36-98", "Bogota", "sofilop")
# usuario_2 = User("Luis", "Fernandez","cra 20 #12-87", "Barranquilla", "luisfdz")
# usuario_3 = User("Catty", "Palacio","Av. san cristobal", "Neiva", "catty")

# usuario_1.describe_user()
# usuario_2.describe_user()
# usuario_3.describe_user()

# usuario_1.greet_user()
# usuario_2.greet_user()
# usuario_3.greet_user()

# ejercicio 9-3
# class User():
#     """clase para modelar un usuario"""

#     def __init__(self, first_name, last_name, address, city, nickname):
#         self.nombre = first_name
#         self.apellido = last_name
#         self.direccion = address
#         self.ciudad = city
#         self.usuario = nickname

#     def describe_user(self):
#         """describe informacion del usuario"""
#         print("\n ----- datos de usuario ------ ")
#         print(f"Nombre ===> {self.nombre} ")
#         print(f"apellidos ===> {self.apellido} ")
#         print(f"direccion ===> {self.direccion} ")
#         print(f"ciudad ===> {self.ciudad} ")
#         print(f"usuario ===> {self.usuario} ")

#     def greet_user(self):
#         """metodo de saludo"""
#         print(f"\nHola {self.nombre} bienvenido a nuesto sitio web!!!")

# ejercicio 9-4
# class Restaurant():
#     """clase para modelar un restaurante"""

#     def __init__(self, restaurant_name, cuisine_type):
#         self.nombre_restaurante = restaurant_name
#         self.tipo_cocina = cuisine_type
#         self.numero_servido = 0

#     def describe_restaurant(self):
#         print(f"nombre del restaurante ==> {self.nombre_restaurante}")
#         print(f"tipo de cocina ==> {self.tipo_cocina}")
#         print(f"numero servido ==> {self.numero_servido}")
    
#     def set_number_served(self, numero):
#         self.numero_servido = numero
    
#     def increment_number_served(self, numero):
#         self.numero_servido += numero

    
#     def open_restaurant(self):
#         print(f"el restaurante {self.nombre_restaurante} ya se encuentra abierto")

# restaurant_1 = Restaurant("Doña petrona", "Comida de mar")
# restaurant_1.describe_restaurant()
# restaurant_1.set_number_served(6)
# restaurant_1.describe_restaurant()
# restaurant_1.increment_number_served(4)
# restaurant_1.describe_restaurant()

#ejercicio 9-5
class User():
    """clase para modelar un usuario"""

    def __init__(self, first_name, last_name, address, city, nickname):
        self.nombre = first_name
        self.apellido = last_name
        self.direccion = address
        self.ciudad = city
        self.usuario = nickname
        self.intentos_login = 0

    def describe_user(self):
        """describe informacion del usuario"""
        print("\n ----- datos de usuario ------ ")
        print(f"Nombre ===> {self.nombre} ")
        print(f"apellidos ===> {self.apellido} ")
        print(f"direccion ===> {self.direccion} ")
        print(f"ciudad ===> {self.ciudad} ")
        print(f"usuario ===> {self.usuario} ")

    def increment_login_attempts(self):
        self.intentos_login += 1


    def reset_login_attempts(self):
        self.intentos_login = 0

    def greet_user(self):
        """metodo de saludo"""
        print(f"\nHola {self.nombre} bienvenido a nuesto sitio web!!!")


# usuario_1 = User("Luisa", "Hernandez","cra 12 #11-16", "codazzi", "sHernandezh")
# usuario_1.describe_user()
# usuario_1.increment_login_attempts()
# usuario_1.increment_login_attempts()
# usuario_1.increment_login_attempts()
# print(usuario_1.intentos_login)
# usuario_1.reset_login_attempts()
# print(usuario_1.intentos_login)

# ejercicio 9-6
# class IceCreamStand(Restaurant):

#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.sabores = ['browny','fresa','chocolate','ron con pasas']

#     def mostrar_sabores(self):
#         print(f"Estos son los sabores que ofrecemos al publico: {self.sabores}")

# helados = IceCreamStand("Galvis",'Heladeria')
# helados.describe_restaurant()
# helados.mostrar_sabores()

# ejercicio 9-8
# class Privileges:

#     def __init__(self, privilegiosx = ["can delete post", "can ban users", "can create users", "can update users"]):
#         self.privileges = privilegiosx
    
#     def show_privileges(self):
#         print(f"\nEstos son los privilegios de Admin: {self.privileges}")



# ejercicio 9-7
# class Admin(User):

#     def __init__(self, first_name, last_name, address, city, nickname):
#         super().__init__(first_name, last_name, address, city, nickname)
#         self.privilegio = Privileges()


# administrador = Admin("Camila", "Fernandez", "Cra 12 - 12-56", "Bogota","camifer")
# administrador.describe_user()
# administrador.privilegio.show_privileges()

# ejercicio 9-7
class Admin(User):

    def __init__(self, first_name, last_name, address, city, nickname):
        super().__init__(first_name, last_name, address, city, nickname)
        self.privileges = ["can delete post", "can ban users", "can create users", "can update users"]
    
    def show_privileges(self):
        print(f"\nEstos son los privilegios de Admin: {self.privileges}")

administrador = Admin("Camila", "Fernandez", "Cra 12 - 12-56", "Bogota","camifer")
administrador.describe_user()
administrador.show_privileges()


