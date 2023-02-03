class Dog:
    """un simple intento para modelar un perro"""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sentarse(self):
        """Simulando a un perro sentandose en respuesta a un comando"""
        print(f"{self.nombre} esta ahora sentado.")

    def darse_vuelta(self):
        """Simulando a un perro dando vueltas en respuesta a un comando"""
        print(f"{self.nombre} esta ahora dando vueltas.")

mi_perro = Dog('Thanos', 2)
tu_perro = Dog('Tony', 5)

print(f"mi perro se llama {mi_perro.nombre}")
print(f"mi perro tiene {mi_perro.edad} año")
mi_perro.sentarse()

print(f"\nTu perro se llama {tu_perro.nombre}")
print(f"Tu perro tiene {tu_perro.edad} año")
tu_perro.sentarse()