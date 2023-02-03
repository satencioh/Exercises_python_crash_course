invitados = ['Pedro', 'Gala', 'Catty', 'Sofia']
print(f'{invitados[0]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[1]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[2]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[3]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'Perdon, {invitados[1]} no podra llegar a la cena')

del(invitados[1])
invitados.insert(1, 'Thanos')
print(invitados)

print('hemos encontrado una mesa aun mas grande ')

invitados.insert(0, 'Laura')
invitados.insert(2, 'Sofia')
invitados.append('Camila')
print(invitados)

print(f'{invitados[0]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[1]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[2]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[3]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[4]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[5]}, estas coordialmente invitado a una espectacular cena esta noche.')
print(f'{invitados[6]}, estas coordialmente invitado a una espectacular cena esta noche.')

print('Ups.. solo podemos invitar a 2 personas')

nombres = invitados.pop()
print(f'{nombres.title()}, no estaras invitado')

nombres = invitados.pop()
print(f'{nombres.title()}, no estaras invitado')

nombres = invitados.pop()
print(f'{nombres.title()}, no estaras invitado')

nombres = invitados.pop()
print(f'{nombres.title()}, no estaras invitado')

nombres = invitados.pop()
print(f'{nombres.title()}, no estaras invitado')

print(f'{invitados[0].title()}, eres uno de los invitados escogido')

print(f'{invitados[1].title()}, eres uno de los invitados escogido')

del(invitados[0])
del(invitados[0])
print(invitados)
