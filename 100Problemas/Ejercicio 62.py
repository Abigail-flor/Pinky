def calificacion(a, b, c):
    return (a+b+c)/3
 
m1 = float(input("Ingrese por favor la calificación de su primer materia: "))
m2 = float(input("Ingrese por favor la calificación de su segunda materia: "))
m3 = float(input("Ingrese por favor la calificación de su tercera materia: "))
promedio = calificacion(m1, m2, m3)
if promedio < 70:
    print("Te vas a extra, por tu promedio de:", promedio)
else:
    print("Tu promedio es de:", promedio)