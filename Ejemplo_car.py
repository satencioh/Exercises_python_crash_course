class Car():
    """Una simple intento para representar un carro"""
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        #estableciendo un valor por defecto de un atributo
        self.kilometraje = 0

    def obtener_descrip_nombre(self):
        nombre_completo = f"{self.anio} {self.marca} {self.modelo}"
        return nombre_completo.title()

    def leer_kilometraje(self):
        print(f"su carro tiene {self.kilometraje} millas")

    def actualizar_kilometraje(self, milaje):
        """
        establece la lectura del kilometraje al valor dado.
        rechaza el cambio si intenta hacer retroceder el kilometraje
        """
        if milaje >= self.kilometraje:
            self.kilometraje = milaje
        else:
            print("no puedes retroceder el kilometraje")
    
    def incrementar_kilometraje(self, millas):
        """agrega la cantidad dada a la lectura del kilometraje"""
        self.kilometraje += millas


# nuevo_carro = Car('audi','a4', 2019)
# print(nuevo_carro.obtener_descrip_nombre())

carro_usado = Car('subaru','outback', 2015)
print(carro_usado.obtener_descrip_nombre())

# para modificar valores de atributos
# - cambiar el valor directamente mediante una instancia
# nuevo_carro.kilometraje = 23
# nuevo_carro.leer_kilometraje()

# - establecer el valor mediante un metodo
# nuevo_carro.actualizar_kilometraje(25)
# nuevo_carro.leer_kilometraje()

carro_usado.actualizar_kilometraje(23_500)
carro_usado.leer_kilometraje()

# - incrementar el valor mediante un metodo
carro_usado.incrementar_kilometraje(100)
carro_usado.leer_kilometraje()