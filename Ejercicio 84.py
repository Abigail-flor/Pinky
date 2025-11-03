try:
    nombre = input("Escribe el nombre del archivo: ")

    with open(nombre, "r") as archivo:
        contenido = archivo.read(5)  # Lee los primeros 5 caracteres

        if len(contenido) < 5:
            raise ValueError("El archivo tiene menos de 5 caracteres.")

        numero = int(contenido)
        print("Número convertido:", numero)

except FileNotFoundError:
    print("Error: el archivo no existe.")
except ValueError:
    print("Error: los primeros 5 caracteres no pueden convertirse a número entero o el archivo es muy corto.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)
