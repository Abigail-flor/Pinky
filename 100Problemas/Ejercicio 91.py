import re

texto = input("Ingresa una cadena con correos electrónicos: ")

usuarios = re.findall(r'([A-Za-z0-9._%+-]+)@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', texto)
print("Nombres de usuario encontrados:", usuarios)
