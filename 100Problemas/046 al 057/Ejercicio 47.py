#Crear listas
materias = []
calificaciones = []
n = int(input("Ingrese la cantidad de materias que va a registrar: "))
for i in range(n):
    materia = str(input("Ingrese la materia: "))
    calificacion = float(input(f"Ingrese la calificación de {materia}: "))
    materias.append(materia) #Se agrega la materia nueva 
    calificaciones.append(calificacion) #Se agrega la calificación de la materia nueva
   
suma = 0
for i in range (n):
    print(f"{materias[i]}: {calificaciones[i]}")
    suma += calificaciones[i] #Se guardara en la suma cada calificación que ingreses a la lista
    promedio = suma/n
print(f"El promedio final es de: {promedio}")
