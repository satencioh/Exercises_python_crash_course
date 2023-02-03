# del modulo car importar la clase Car
from car import Car

my_new_car = Car('audi','a4', 2019)
print(my_new_car.obtener_descrip_nombre())

my_new_car.kilometraje = 23
my_new_car.leer_kilometraje()