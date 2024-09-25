 # Pokédex Application
## Overview
The Pokédex application is a web-based application that allows users to explore Pokémon data 
from various generations. Users can search for Pokémon by name or ID, and sort them based on 
different attributes such as ID, weight, and height.

## Features
- **Search Functionality:** Filter Pokémon by name or ID.
- **Sorting Options:** Sort Pokémon by ID, weight, or height.
- **Dynamic Display:** Show Pokémon details, including type, height, weight, and an image.
- **Responsive Design:** The app is optimized for both desktop and mobile devices.

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Data Source:** PokéAPI (RESTful API or GraphQL API)
- **Libraries:** Font Awesome for icons

## Getting Started

### Prerequisites
- Python 3.12
- Flask
- Required Python libraries (can be installed via `pip`)

### How to run the application

REMINDER: When re-running the application with modifications, remember to 
delete pokemon_data.json and then run the application! 

1. Download zip file and unzip contents
2. Head into the "Pokedex" directory
3. Create Python virtual environment using the following commands:
    - python -m venv venv
    - virtualenv venv
4. Ensure Flask is downloaded by running:
    - pip install flask
5. Run the application using:
    - python app.py
6. Go to http://127.0.0.1:5000/
