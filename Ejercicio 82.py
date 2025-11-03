try:
    with open("a.txt", "r") as archivo_a:
        contenido_a = archivo_a.read()

    with open("b.txt", "r") as archivo_b:
        contenido_b = archivo_b.read()

    with open("combinado.txt", "w") as combinado:
        combinado.write(contenido_a + "\n" + contenido_b)

    print("Los archivos se combinaron en 'combinado.txt'.")
except FileNotFoundError:
    print("Error: uno de los archivos ('a.txt' o 'b.txt') no existe.")
