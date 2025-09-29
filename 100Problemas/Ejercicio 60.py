def sumatoria(lista):
    return sum(lista)

def promedio():
    n = int(input("Por favor, ingrese la cantidad de numeros que desea sumar para promediar: "))
    lista = []
    for i in range (n):
        numeros = float(input(f"Ingrese el numero {i+1}: "))
        lista.append(numeros)
        
    resultado = sumatoria(lista)
    return resultado/len(lista)

print(f"Su promedio es: {promedio()}")
    