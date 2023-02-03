users = {
    'aeinstein':{
        'nombre':'albert',
        'apellido':'einstein',
        'ubicacion':'princeton'
    },
    'mcurie':{
        'nombre':'marie',
        'apellido':'mcurie',
        'ubicacion':'paris'
    }
}

for user, user_info in users.items():
    print(f"\nUsuario: {user}")
    nombre_completo = f"{user_info['nombre']} {user_info['apellido']}"
    ubicacion = user_info['ubicacion']

    print(f"\tNombre completo: {nombre_completo.title()}")
    print(f"\tUbicacion: {ubicacion.title()}")