#Importar las librerias que nos piden
import numpy as np
from scipy.integrate import quad

#Hacer la funcion de la ecuacion y que devuelva la operacion
def f(x):
	return np.sin(x**2)

#Intervalo
a = 0
b = 2

#Hacer la operacion con su respuesta y su error
respuesta, error = quad(f, a, b)
print("Resultado de la integral")
print(round(respuesta, 5))
print("\nError")
print(round(error, 5))