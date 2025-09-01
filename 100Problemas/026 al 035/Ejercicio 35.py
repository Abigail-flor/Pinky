#Ej.Orden descendente de tres números

#Números
x = int(input("Ingrese un primer número entero: "))
y = int(input("Ingrese un segundo número entero: "))
z = int(input("Ingrese un tercer número entero: "))

#Comparaciones
if x>=y and x>=z:
    if y>=z:
      print(x, y, z)
    else:
      print(x, z, y)
elif y>=x and y>=z:
   if x>=z:
      print(y, x, z)
   else:
      print(y, z, x)
else:
    if x>=y:
      print(z, x, y)
    else:
      print(z, y, x)