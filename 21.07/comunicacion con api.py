import requests

res = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")

print(res.status_code)

json = res.json()

print(jason)




