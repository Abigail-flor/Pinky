#Ej.Cálculo de beneficio

#Ingresar información de venta
precioDeVenta = float(input("Por favor, ingrese el precio de venta "))
cantidadVendida = int(input("¿Cuántos productos se vendieron? "))
costoFijo = float(input("¿Cuál es el costo fijo? "))
costoVariable = float(input("¿Cuánto cuesta producir una pieza? "))

#Operaciones
ingresoTotal = precioDeVenta*cantidadVendida
costoTotal = costoFijo + (cantidadVendida*costoVariable)
beneficio = ingresoTotal-costoTotal

#Resultado
print(f"El beneficio total de tus ingresos es de: ${beneficio}")