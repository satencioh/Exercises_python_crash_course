alien_0 = {'color':'green', 'speed': 'slow'}

#get() para obtener el valor de una llave y en caso de no existir retorna un
#mensaje definido
point_value = alien_0.get('points','no se asigna ningun valor en puntos')
print(point_value)