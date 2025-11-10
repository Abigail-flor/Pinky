import re

correo = input("Ingresa un correo electrónico: ")
if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', correo):
    print("Válido")
else:
    print("Inválido")
