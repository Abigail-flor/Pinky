print("Bienvenido")
import math
def factoriales():
    lista = []
    n = int(input("Ingrese la cantidad de numeros que necesiten sacar el factorial: "))
    for i in range(n):
        num = int(input(f"Por favor, ingrese el número {i+1}: "))
        factorial = math.factorial(num)
        lista.append(factorial)
    print(f"Factoriales calculados: {lista}")
factoriales()