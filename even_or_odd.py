number = input("Ingresa un numero, y te dire si es par o impar: ")
number = int(number)

if number % 2 == 0:
    print(f"el numero {number} es par")
else:
    print(f"el numero {number} es impar")