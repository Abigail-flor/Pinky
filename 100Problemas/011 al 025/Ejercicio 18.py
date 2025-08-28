#Ej.Operaciones matemáticas

#Ingresar números
a = float(input("Ingresa el primer número "))
b = float(input("Ingresa el segundo número "))

#Calcular operaciones
suma = a + b
resta = a - b
multi = a * b

if b != 0:
 division = a/b
 modulo = a % b
else:
 division = "Error"
 modulo = "Error"

potenciacion = a**b

if a >= 0:
 raiz = a ** 0.5
else:
 raiz = "Error"

#Mostrar en pantalla resultados
print(f"La suma fue de: {suma}")
print(f"La resta fue de: {resta}")
print(f"La multiplicación fue de: {multi}")
print(f"La división fue de: {division}")
print(f"El primer número elevado al segundo fue de: {potenciacion}")
print(f"La raíz cuadrada del primero es de: {raiz}")
print(f"El módulo es de: {modulo}")
