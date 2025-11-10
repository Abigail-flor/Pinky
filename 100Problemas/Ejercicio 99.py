import requests

numero = input("Ingresa un número: ")

# Construir la URL con f-string
url = f"https://numbersapi.com/{numero}?json"

respuesta = requests.get(url)
datos = respuesta.json()

print("Trivia:", datos["text"])
