try:
    with open("numeros.txt", "r") as archivo:
        lineas = archivo.readlines()

    numeros = []
    for linea in lineas:
        try:
            num = float(linea.strip())
            numeros.append(num)
        except ValueError:
            print(f"Advertencia: '{linea.strip()}' no es un número válido.")

    if len(numeros) == 0:
        print("No hay números válidos para calcular el promedio.")
    else:
        promedio = sum(numeros) / len(numeros)
        print("El promedio es:", promedio)
except FileNotFoundError:
    print("Error: el archivo 'numeros.txt' no existe.")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
