import re

texto = input("Ingresa una cadena de texto: ")
palabras = re.findall(r'\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]*', texto)
print("Palabras que comienzan con mayúscula:", palabras)
