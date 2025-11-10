import requests

url = "https://api.dictionaryapi.dev/api/v2/entries/en/example"
respuesta = requests.get(url)
datos = respuesta.json()

# Navegar el JSON
palabra = datos[0]["word"]
definicion = datos[0]["meanings"][0]["definitions"][0]["definition"]

print("Palabra:", palabra)
print("Definición principal:", definicion)
