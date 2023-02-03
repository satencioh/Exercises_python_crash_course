#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#change the value in the index 0
#motorcycles[0] = 'ducati'
#print(motorcycles)

#add new element in the end the list
#motorcycles.append('ducati')
#print(motorcycles)

#add several items in the a empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

#print(motorcycles)

#inserting elements into a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

#removing an item usgind del statement
#del motorcycles[0]
#print(motorcycles)

#el metodo pop remueve el ultimo elementos de la lista
# o permite guardar ese valor
#popped_motor = motorcycles.pop()
#print(motorcycles)
#print(popped_motor)

#last_owned = motorcycles.pop()
#print(f'The last motorcycle I owned was a {last_owned.title()}.')

#remove permite remover un item por el valor
motorcycles.remove('ducati')
print(motorcycles)
