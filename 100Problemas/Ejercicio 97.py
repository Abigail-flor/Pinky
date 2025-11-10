import requests
import json

url = "https://api.github.com"
respuesta = requests.get(url)

datos = respuesta.json()

# Guardar la respuesta en un archivo con formato bonito
with open("respuesta.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, ensure_ascii=False, indent=4)

print("Respuesta guardada en 'respuesta.json'")
