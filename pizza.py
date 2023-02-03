# * crea una tupla
def hacer_pizza(size, *toppings):
    print(f"\nHaciendo una pizza {size}-cm con los siguientes toppings: ")
    for topping in toppings:
        print(f" - {topping.title()}")
