
import os

carpeta = input("Por favor, ingrese el nombre de la carpeta que desea encontrar: ")

if os.path.isdir(carpeta):
    archivos = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".csv"):
            archivos.append(archivo)
    
    archivos.sort()
  
    print("Archivos hallados con terminación .csv:")
    for nombre in archivos:
        print("*", nombre)
else:
    print("Esa carpeta no existe")
