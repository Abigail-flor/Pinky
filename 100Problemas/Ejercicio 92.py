import re

texto = input("Ingresa un párrafo: ")

# Separar por punto, signo de exclamación o interrogación
oraciones = re.split(r'[.!?]\s*', texto)

# Eliminar vacíos y mostrar cada oración
print("Oraciones:")
for o in oraciones:
    if o.strip():
        print(o.strip())
