import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true"
respuesta = requests.get(url)
datos = respuesta.json()

# Extraer datos del clima
temp = datos["current_weather"]["temperature"]
viento = datos["current_weather"]["windspeed"]

print("Temperatura actual:", temp, "°C")
print("Velocidad del viento:", viento, "km/h")
