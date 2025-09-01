#Ej.Evaluación de vendedor según volumen de ventas

#Datos
nombre = str(input("Ingrese el nombre del vendedor: "))
volumen = float(input("Ingrese el volumen de venta en pesos: "))

#Definir su situacón laboral
if volumen < 1000:
    print(f"El vendedor {nombre}, está: DESPEDIDO")
elif volumen >= 1000 and volumen <= 4999.99:
    print(f"El vendedor {nombre}, está en: PERIODO DE PRUEBA")
elif volumen >= 5000 and volumen <= 9999.99:
    print(f"El vendedor {nombre}, tiene un: BONO DEL 5% ")
else:
    print(f"El vendedor {nombre}, tiene un: BONO DEL 10%")