try:
    nombre = input("Escribe tu nombre: ")
    edad = input("Escribe tu edad: ")
    carrera = input("Escribe tu carrera: ")

    with open("perfil.txt", "w") as archivo:
        archivo.write(nombre + "\n")
        archivo.write(edad + "\n")
        archivo.write(carrera + "\n")

    print("Datos guardados en 'perfil.txt'.")
except Exception as e:
    print("Ocurrió un error al guardar el archivo:", e)
