sin_confirmar = ['mateo', 'paola', 'carolina']
confirmados = []

#se ejecuta mientras la lista no este vacia
while sin_confirmar:
    usuario_reciente = sin_confirmar.pop()

    print(f"Verificando usuario: {usuario_reciente.title()}")
    confirmados.append(usuario_reciente)

print("\nLos siguientes usuarios han sidos connfirmados: ")

for user in confirmados:
    print(user.title())