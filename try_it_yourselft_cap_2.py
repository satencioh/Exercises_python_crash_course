foods = ['pizza','falafel','carrot cake','ice cream','kitkat']

# for food in foods[:3]:
#     print(food)

# for food in foods[2:]:
#     print(food)

# for food in foods[-3:]:
#     print(food)

pizzas = ['hawaiana','pollo-champiñon','mexicana','peperoni']

friends_pizzas = pizzas[:]
pizzas.append('italiana')
friends_pizzas.append('vegetariana')

# for pizza in pizzas:
#     print(f"I like {pizza.title()} pizza")
print("My favorite food are: ")

for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite food are: ")


for pizza in friends_pizzas:
    print(pizza
    )