respuestas = {}
encuesta_activa = True

while encuesta_activa:
    nombre = input("\nCual es tu nombre? ")
    respuesta = input("Cual montaña te gustaria escalar algun dia? ")

    respuestas[nombre] = respuesta

    repeticion = input("Te gustaria dejar que otra persona responda? (yes / no) ")
    if repeticion == 'no':
        encuesta_activa = False

print("\n--- Resultado de la encuesta ---")
for n, r in respuestas.items():
    print(f"{n.title()} le gustaria escalar en {r}.")