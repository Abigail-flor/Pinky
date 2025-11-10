import requests

url = "https://pokeapi.co/api/v2/pokemon/25"
respuesta = requests.get(url)
datos = respuesta.json()

nombre = datos["name"]
tipos = [t["type"]["name"] for t in datos["types"]]

print("Nombre del Pokémon:", nombre.capitalize())
print("Tipos:", ", ".join(tipos))
