def EsMultiplo(a, b):
    if a % b == 0:
        return f"{a} si es multiplo de {b}"
    else:
        return f"{a} no es multiplo de {b}"
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
print(EsMultiplo(a, b))