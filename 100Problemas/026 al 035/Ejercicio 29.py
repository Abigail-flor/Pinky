#Ej.División segura

#Ingresar números
x = float(input("Ingrese el número que quiere dividir: "))
y = float(input("Ingrese el número por el que lo quiere dividir: "))

#Comparación
if y == 0:
    print("La operación está indefinida")
else:
    d = x/y
    print(f"El resultado es: {d}")