import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd27ae6fc8bf8134763450983f8141e4f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

body_edit_name = {
    "pokemon_id": "109101",
    "name": "generate",
    "photo_id": -1
}

body_add_pokeball = {
    "pokemon_id": "109101"
}

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.json())

response_edit_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_edit_name)
print(response_edit_name.json())

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.json())

