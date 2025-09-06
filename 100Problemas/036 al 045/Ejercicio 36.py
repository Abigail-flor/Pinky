#Ej.Repetir elevación al cuadrado

numero = float(input("Ingrese un número que desee elevar al cuadrado: "))
x = numero**2
print(f"Tu número elevado al cuadrado es {x}")
y = str(input("¿Deseas ingresar otro número?: "))
while y == "si" or y == "Si":
    numero = float(input("Ingrese un número que desee elevar al cuadrado: "))
    x = numero**2
    print(f"Tu número elevado al cuadrado es: {x}")
    y = str(input("¿Deseas ingresar otro número?: "))
    while y=="no" or y=="No":
       print("Usted ha terminado el cálculo")
       break