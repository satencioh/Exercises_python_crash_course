places = ['miami','españa','toronto','new york','orlando']
print(f'Esta es la lista original:{places}')
print(f'\nAqui es la lista ordenada:{sorted(places)}')
print(f'\nLista conservando su orden original:{places}')
print(f'\nAqui es la lista ordenada reversa:{sorted(places, reverse=True)}')
print(f'\nLista conservando su orden original:{places}')
places.reverse()
print(f'\nLista reverse original:{places}')
places.reverse()
print(f'\nLista estado original:{places}')
places.sort()
print(f'\nLista original orden alf:{places}')
places.sort(reverse=True)
print(f'\nLista original orden alf en reverse:{places}')

invitados = ['Luis', 'Gala', 'Catty', 'Carla']
print(f'{len(invitados)} personas seran invitadas a la cena')