import re

texto = input("Ingresa una cadena con números: ")
numeros = re.findall(r'\d*\.\d+|\d+', texto)
numeros = [float(n) for n in numeros]
print("Números encontrados:", numeros)
