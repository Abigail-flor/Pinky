try:
    with open("entrada.txt", "r") as archivo:
        numero = 1
        for linea in archivo:
            print(f"Línea {numero}: {linea.strip()}")
            numero += 1
except FileNotFoundError:
    print("Error: el archivo 'entrada.txt' no existe.")
