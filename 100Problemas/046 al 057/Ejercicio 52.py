#Crear la listas
productos = ["shampoo", "mesa", "mantel", "jabón", "toper"]
precios = [55, 1200, 39, 20.9, 48.5]
ventas = [10, 3, 8, 22, 15]

#Hacer las operaciones a calcular
for i in range(len(productos)):
    ingresos = ventas[i]*precios[i]
    print(f"Producto: {productos[i]}, Precio: {precios[i]}, Ventas: {ventas[i]}, Ingresos: ${ingresos}")
