def imprimir_modelo(diseño_sinimp, modelo_completado):
    while diseño_sinimp:
        diseño_reciente = diseño_sinimp.pop()
        print(f"imprimiendo modelo: {diseño_reciente}")
        modelo_completado.append(diseño_reciente)

def mostrar_modelos(modelo_completado):
    print("\nLos siguientes modelos han sido impresos")
    for modelo in modelo_completado:
        print(modelo)


# diseño_sinimp =['casa arquitectonica','zapato ortopedico', 'gafas medicas']
# modelo_completado = []

# imprimir_modelo(diseño_sinimp, modelo_completado)
# mostrar_modelos(modelo_completado)