# ** crea un diccionario
def contruir_perfil(nombre, apellido, **info_adicional):
    info_adicional['nombre'] = nombre
    info_adicional['apellido'] = apellido
    return info_adicional

perfil_usuario = contruir_perfil('maria', 'lopez', ubicacion='codazzi', profesion='psicologa')

print(perfil_usuario)