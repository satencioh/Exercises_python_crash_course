class Restaurant():
    """clase para modelar un restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        self.nombre_restaurante = restaurant_name
        self.tipo_cocina = cuisine_type

    def describe_restaurant(self):
        print(f"nombre del restaurante {self.nombre_restaurante}")
        print(f"tipo de cocina {self.tipo_cocina}")
    
    def open_restaurant(self):
        print(f"el restaurante {self.nombre_restaurante} ya se encuentra abierto")