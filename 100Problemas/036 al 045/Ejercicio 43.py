#Ej.Acumulador de abonos

abono = 100000
acumulado = 0

while acumulado < abono:
  dinero = float(input("Ingrese la cantidad que desea abonar: "))
  acumulado += dinero
  print(f"Su dinero acumulado es de: {acumulado}")

print("¡Has llenado tu abono!")