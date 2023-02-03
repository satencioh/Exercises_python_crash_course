#la palabra with cierra el archivo una vez que ya no sea necesario
# with open('pi_digits.txt') as archivo:
#     contenido = archivo.read()
# print(contenido.rstrip())

# filename = 'pi_digits.txt'

# with open(filename) as archivo:
#     for line in archivo:
#         print(line.rstrip())

# with open(filename) as f:
#     lines = f.readlines()

# for line in lines:
#     print(line.rstrip())

# pi_string = ' '
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

filename_2 = 'pi_million_digits.txt'

with open(filename_2) as f:
    lines = f.readlines()

pi_string = ' '
for line in lines:
    pi_string += line.strip()

# print(f"{pi_string[:52]}...")

birthday = input("ingresa la fecha de tus cumpleaños, cumpliendo el formato mmddyy: ")
if birthday in pi_string:
    print("tus cumpleaños aparecen en el primer millon de digitos de PI")
else:
    print("tus cumpleaños no aparecen en el primer millon de digitos de PI")