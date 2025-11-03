try:
    frase = input("Escribe una frase: ")

    # Abrir en modo 'a' para agregar al final sin borrar lo anterior
    with open("registro.txt", "a") as archivo:
        archivo.write(frase + "\n")

    print("Frase agregada al archivo 'registro.txt'.")
except Exception as e:
    print("Ocurrió un error al escribir en el archivo:", e)
