#Llamar a la librería pandas
import pandas as pd

#Crear listas para guardar informacion
producto = ["bimbo", "alpura", "suavitel", "pachoncito"]
precio = [45, 27, 72, 103] 
cantidad = [400, 350, 273, 321]

#Hacer el frame con forma de diccionario para guardae los nombres con ayuda de .DataFrame de pandas
frame = pd.DataFrame({
"Productos": producto,
"Precios": precio,
"Cantidad": cantidad
})
#Imprimir las tablas de frame
print("Frame")
print(frame)
#Imprimir los princupales estadisticos con ayuda de .describe
print("\n-Principales estadisticos-")
print(frame.describe())