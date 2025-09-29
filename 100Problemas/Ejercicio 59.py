def sumatoria():
    n = int(input("Por favor, ingrese la cantidad de números que desea sumar: "))
    lista = []
    for i in range(n):
        numeros = float(input(f"Ingrese el número {i+1}: "))
        lista.append(numeros)   
    return sum(lista)  
    
resultado = sumatoria()   
print(f"La sumatoria es: {resultado}")