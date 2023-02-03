# prompt = "si tu nos dices quien eres, nosotros podemos personalizar los mensajes que tu ves"
# prompt += "\ncual es tu primer nombre?"

# name = input(prompt)
# print(f"\nHola, {name.title()}")

altura = input("cual es tu altura en pulgadas? ")
altura = int(altura)
if altura >= 48:
    print("\nTu eres muy alto")
else:
    print("\nTu eres muy bajo")