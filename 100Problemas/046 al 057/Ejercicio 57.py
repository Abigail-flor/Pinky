# Lista de ejemplo
lista = [5, 10, 15, 20, 25, 30]

# Solicitar el valor a buscar
valor = int(input("Ingrese el valor que desea buscar: "))

# Variable para saber si se encontró
encontrado = False

# Recorrer la lista manualmente
for i in range(len(lista)):
    if lista[i] == valor:
        print(f"El valor {valor} se encuentra en la lista en el índice {i}.")
        encontrado = True
        break  # Opcional: detener la búsqueda al encontrarlo

# Si no se encontró
if not encontrado:
    print(f"El valor {valor} no está en la lista.")