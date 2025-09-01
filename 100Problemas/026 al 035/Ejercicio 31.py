#Ej.Evaluación académica

#Calificación
calificacion = float(input("Ingrese su calificación: "))

#Comparaciones
if calificacion < 6:
    print("El estatus del alumno es: IRREGULAR")
elif calificacion > 6 and calificacion < 9.9:
    print("El estatus de alumno es: REGULAR")
else:
    print("El estatus del alumno es de: EXCELENCIA")