#Ej.Área o perímetro de un cuadrado

#Opciones
op = int(input("Escoja una opción:\n1.-Área\n2.-Perímetro\n3.-Salir "))

#Calcular
if op == 1:
    l = float(input("ingrese la longitud de su lado: "))
    A = l*2
    print(f"El área del cuadrado es: {A}")
elif op == 2:
    l = float(input("Ingrese la longitud de su lado: "))
    P = l*4
    print(f"El perímetro de su cuadrado es: {P}")
elif op == 3:
  print("Usted ha terminaddo")
else:
  print("Ingrese una opción válida")