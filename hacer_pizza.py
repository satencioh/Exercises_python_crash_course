#importar todo el modulo
#import pizza 

# pizza.hacer_pizza(16, 'peperoni')
# pizza.hacer_pizza(20, 'camarones','champiñones','queso')

#importar una funcion del modulo
#from pizza import hacer_pizza


# hacer_pizza(16, 'peperoni')
# hacer_pizza(20, 'camarones','champiñones','queso')


#importar una funcion del modulo y colocandole alias
# from pizza import hacer_pizza as hpz

# hpz(16, 'peperoni')
# hpz(20, 'camarones','champiñones','queso')

#importar el modulo aplicando alias
#import pizza as p

# p.hacer_pizza(16, 'peperoni')
# p.hacer_pizza(20, 'camarones','champiñones','queso')

#importar todas las funciones en un modulo
from pizza import *

hacer_pizza(16, 'peperoni')
hacer_pizza(20, 'camarones','champiñones','queso')