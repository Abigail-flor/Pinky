import sys
import os

# Si no se pasan argumentos por la terminal, pedirlos con input()
if len(sys.argv) == 1:
    nombre_archivo = input("Nombre del archivo: ")
    n_str = input("Número de líneas: ")
else:
    nombre_archivo = sys.argv[1]
    n_str = sys.argv[2]

# Verificaciones
if not os.path.isfile(nombre_archivo):
    print(f"Error: el archivo '{nombre_archivo}' no existe.")
    sys.exit(1)

if not n_str.isdigit():
    print("Error: el segundo argumento debe ser un número entero.")
    sys.exit(1)

n = int(n_str)

# Leer e imprimir las primeras n líneas
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for i, linea in enumerate(lineas[:n], start=1):
        print(f"{i}: {linea.strip()}")
