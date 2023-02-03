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

#clase hija -> aplica herencia
class EletricCar(Car):
    """representa aspectos de un carro, especifico a carros electricos"""

    def __init__(self, marca, modelo, anio):
        """- Iniciaiza atributos de la clase padre
            - inicia atributos especificos de un carro electrico 
        """
        super().__init__(marca, modelo, anio)
        self.bateria = 75

    def describir_bateria(self):
        """imprimir una declaracion que describe el tamano de la bateria"""
        print(f"Este carro tiene una bateria {self.bateria}-kWh")
