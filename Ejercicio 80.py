try:
    with open("origen.txt", "r") as origen:
        contenido = origen.read()

    with open("copia.txt", "w") as copia:
        copia.write(contenido)

    print("El contenido se copió correctamente a 'copia.txt'.")
except FileNotFoundError:
    print("Error: el archivo 'origen.txt' no existe.")
