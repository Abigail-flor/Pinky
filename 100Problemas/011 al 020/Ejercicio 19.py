#Ej.Promedio y datos del alumno

#Recibir los datos
nombre = str(input("Por favor, ingrese el nombre del alumn@: "))
num_boleta = int(input("Ingrese el número de  boleta "))
cal1 = float(input("Ingrese la calificación 1 "))
cal2 = float(input("Ingrese la calificación 2 "))
cal3 = float(input("Ingrese la calificación 3 "))
cal4 = float(input("Ingrese la calificación 4 "))
cal5 = float(input("Ingrese la calificación 5 "))

#Calcular promedio
promedio = (cal1 + cal2 + cal3 + cal4 + cal5)/5

print(f"El estudiante de nombre: {nombre}, en la boleta Num. {num_boleta}, obtuvo un promedio de: {promedio}")