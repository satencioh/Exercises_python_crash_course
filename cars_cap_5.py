cars = ['bmw','audi','toyota','subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")