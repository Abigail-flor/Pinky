import re

texto = input("Ingresa un texto: ")

# Lista de palabras prohibidas
prohibidas = ["tonto", "feo", "idiota", "bobo"]

# Reemplazar cada palabra (sin importar mayúsculas/minúsculas)
for palabra in prohibidas:
    patron = re.compile(rf'\b{palabra}\b', re.IGNORECASE)
    texto = re.sub(patron, "*" * len(palabra), texto)

print("Texto censurado:")
print(texto)
