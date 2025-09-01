#Ej.Clasificación por edad

#Edad
edad = int(input("¿Cuántos años tiene el individuo?: "))

#Clasificaciones
if edad<0 or edad > 120:
    print("Edad inválida")
elif edad<10:
    print("Es un pequeño niño, un menor de edad")
elif edad>=10 and edad<=17:
    print("Es un joven adolescente, un menor de edad")
elif edad>=18 and edad <= 29:
    print("Es un joven, mayor de edad")
elif edad>=30 and edad <= 59:
    print("Es un adulto, mayor de edad")
else:
    print("Es un adulto mayor, mayor de edad")