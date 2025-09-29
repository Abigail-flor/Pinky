def perimetro(a, b):
    return 2*(b + a)
#Pedir datos del usuario
base = float(input("Ingrese el valor de su base: "))
altura = float(input("Ingrese el valor de su altura: "))
resultado = perimetro(base, altura)
print("Su perímetro es:", resultado)