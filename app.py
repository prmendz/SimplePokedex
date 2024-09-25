from flask import Flask, render_template, jsonify
import requests
import json
import os

app = Flask(__name__)

POKEAPI_BASE_URL = 'https://pokeapi.co/api/v2/'
JSON_FILE = 'pokemon_data.json'

# Fetch the first 151 Pokémon data and save to JSON
def fetch_and_save_pokemon_data():
    pokemon_list = {}
    generations = {
        1: range(1, 152),  # Kanto
        2: range(152, 252),  # Johto
        3: range(252, 387),  # Hoenn
        4: range(387, 494),  # Sinnoh
        5: range(494, 650),  # Unova
        6: range(650, 722),  # Kalos
        7: range(722, 810),  # Alola
        8: range(810, 898)   # Galar
    }

    for gen, ids in generations.items():
        pokemon_list[gen] = []
        for id in ids:
            try:
                response = requests.get(f'{POKEAPI_BASE_URL}pokemon/{id}')
                response.raise_for_status()  # Raise an error for bad responses
                data = response.json()
                pokemon = {
                    'id': data['id'],
                    'name': data['name'],
                    'types': [t['type']['name'] for t in data['types']],
                    'height': data['height'],
                    'weight': data['weight'],
                    'image': data['sprites']['front_default'],
                    'url': f'https://www.pokemon.com/us/pokedex/{data["name"]}'  # Direct link to the Pokémon's page
                }
                pokemon_list[gen].append(pokemon)
                if len(pokemon_list[gen]) == 60:  # Stop after 60 Pokémon
                    break
            except requests.exceptions.RequestException as e:
                print(f"Error fetching Pokémon ID {id}: {e}")

    # Save the data to a JSON file
    with open(JSON_FILE, 'w') as f:
        json.dump(pokemon_list, f, indent=4)

# Load Pokémon data from the JSON file
def load_pokemon_data():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    else:
        fetch_and_save_pokemon_data()
        return load_pokemon_data()  # Load the data again after fetching

@app.route('/')
def index():
    pokemon_list = load_pokemon_data()
    # Keep only the first 3 Pokémon from each generation for initial display
    initial_pokemon = {gen: data[:3] for gen, data in pokemon_list.items()}
    return render_template('index.html', pokemon_list=initial_pokemon, all_pokemon=pokemon_list)

@app.route('/api/pokemon-list')
def api_pokemon_list():
    pokemon_list = load_pokemon_data()
    return jsonify(pokemon_list)

def load_pokemon_data():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
            print("Loaded Pokémon data:", data)  # Debug line
            return data
    else:
        fetch_and_save_pokemon_data()
        return load_pokemon_data()

@app.route('/generation/<int:gen>')
def show_generation(gen):
    pokemon_list = load_pokemon_data()
    print(gen)
    all_pokemon = pokemon_list.get(str(gen), [])
    print(f"Generation {gen} Pokémon: {all_pokemon}")  # Debug line
    return render_template('generation.html', pokemons=all_pokemon, generation=gen)

if __name__ == '__main__':
    app.run(debug=True)
