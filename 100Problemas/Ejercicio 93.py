import requests

url = "https://numbersapi.com/42?json"
respuesta = requests.get(url)

# Convertir la respuesta a formato JSON
datos = respuesta.json()

# Mostrar el texto de la trivia
print("Trivia:", datos["text"])
