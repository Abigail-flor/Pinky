import requests

url = "https://api.github.com"
respuesta = requests.get(url)

print("Código de estado:", respuesta.status_code)

if respuesta.status_code == 200:
    print("Todo bien")
else:
    print("Hubo un problema")
