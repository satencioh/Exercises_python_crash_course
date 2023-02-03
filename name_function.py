
# def get_formatted_name(first, last):
#     """Generar un nombre bien formateado"""
#     full_name = f"{first} {last}"
#     return full_name.title()

def get_formatted_name(first, last, middle=''):
    """Generar un nombre bien formateado"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()