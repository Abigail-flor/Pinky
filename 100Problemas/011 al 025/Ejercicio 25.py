#Ej.Ecuación de la recta

#Ingresar datos
x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

#Operación
if x1 - x2 != 0:
    m = (y1 - y2)/(x1 - x2)
    b = y1 - m*x1
    print(f"La ecuación de la recta es: y = {round(m,2)}x + {round(b,2)} ")
else: 
    print(f"La recta no tiene pendiente, es vertical: x = {x1}")