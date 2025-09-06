#Ej.Calculadora básica con repetición

numero = float(input("Ingrese un número que quieres usar: "))
numero2 = float(input("Inrese el segundo numero que quiere usar: "))
multi = numero*numero2
suma = numero+numero2
resta = numero-numero2
if numero2 != 0:
 division = numero/numero2
 modulo = numero%numero2
else:
  division = "Esta indefinida la division"
  modulo = "No es posible calcular con 0"
exponente = numero**numero2
print(f"La suma es de: {suma}, la resta es de: {resta}")
print(f"La multiplicación es de: {multi}, la división es de: {division}")
print(f"El exponente es:{exponente} y el módulo es: {modulo}")
respuesta=str(input("¿Desea hacer más operaciones?"))
while respuesta.lower()=="si":
   numero = float(input("Ingrese un número que quieres usar: "))
   numero2 = float(input("Inrese el segundo numero que quiere usar: "))
   multi = numero*numero2
   suma = numero+numero2
   resta = numero-numero2
   if numero2 != 0:
     division = numero/numero2
     modulo = numero%numero2
   else:
     division = "Esta indefinida la division"
     modulo = "No es posible calcular con 0"
   exponente = numero**numero2
   print(f"La suma es de: {suma}, la resta es de: {resta}")
   print(f"La multiplicación es de: {multi}, la división es de: {division}")
   print(f"El exponente es:{exponente} y el módulo es: {modulo}")
   respuesta=str(input("¿Desea hacer más operaciones?"))

print("Ha terminado sus operaciones")
