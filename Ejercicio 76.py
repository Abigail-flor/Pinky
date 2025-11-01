import matplotlib.pyplot as plt

# Datos a graficar
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Crear la gráfica
plt.plot(x, y, 'o-', color='blue')  # 'o-' = círculos conectados con líneas

# Agregar título y etiquetas
plt.title("Gráfica de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Guardar la gráfica como archivo PNG
plt.savefig("grafica.png")

# Mostrar la gráfica en pantalla
plt.show()
