# requests = ['mushrooms','green peppers','extra cheese']
# requests = []
# if 'mushrooms' in request:
#     print(f"agregando {request[0]}")
# if 'Pepperoni'in request:
#     print(f"agregando Pepperoni")
# if 'extra cheese'in request:
#     print(f"agregando {request[1]}")

# print("\nTermine de hacer su pizza")

# for request in requests:
#     print(f"agregando {request}.")

# print("\nTermine de hacer tu pizza!")
# python retorna True si una lista tiene elemento, de lo contrario retorna False
# if requests:
#     for request in requests:
#         print(f"agregando {request}.")
#     print("\nTermine de hacer tu pizza!")
# else:
#     print("Quiere una pizza sencilla?")

ingredientes_disp = ['mushrooms','olives', 'green peppers', 'pepperoni', 'pineapple','extra cheese']

ingredientes_solic = ['mushrooms','french fries','extra cheese']

for ingrediente in ingredientes_solic:
    if ingrediente in ingredientes_disp:
        print(f"agregando {ingrediente}.")
    else:
        print(f"lo sentimos, no tenemos {ingrediente}.")

print("\nTermine de hacer tu pizza!")