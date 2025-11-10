import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=5"
respuesta = requests.get(url)
datos = respuesta.json()

print("Primeros 5 Pokémon:")
for pokemon in datos["results"]:
    print("-", pokemon["name"].capitalize())
