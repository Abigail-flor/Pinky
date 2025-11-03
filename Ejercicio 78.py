try:
    with open("datos.txt", "r") as archivo:
        lineas = archivo.readlines()

        total_lineas = len(lineas)
        total_palabras = 0
        total_caracteres = 0

        for linea in lineas:
            palabras = linea.split()
            total_palabras += len(palabras)
            total_caracteres += len(linea)

        print("Líneas:", total_lineas)
        print("Palabras:", total_palabras)
        print("Caracteres:", total_caracteres)
except FileNotFoundError:
    print("Error: el archivo 'datos.txt' no existe.")
