#Ej.Comparar dos números

#Números
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

#Comparar
if a>b:
    print("El primer número es mayor que el segundo")
else:
    if b>a:
        print("El segundo número es mayor que el primero")
    else:
        print("Los números son iguales")
