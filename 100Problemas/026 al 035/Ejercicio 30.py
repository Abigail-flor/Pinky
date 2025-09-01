#Ej.Análisis de beneficios

#Datos
precio_unit = float(input("Ingrese el precio unitario del producto: "))
cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
egresos = float(input("Ingrese los costos totales: "))

#Operacioes
ingresos = (precio_unit)*(cantidad_vendida)

#Comparaciones
if ingresos<egresos:
    print("Su empresa está tendiendo perdidas")
elif ingresos == egresos:
    print("Su empresa está en un punto de equilibrio")
else:
    print("Su empresa esta generando ganancias")