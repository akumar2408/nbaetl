# scripts/extract.py
import json
import requests
from config import config, secrets

def extract(game_id):
    url = config.API_URL
    headers = {
        "X-RapidAPI-Key": secrets.RAPIDAPI_KEY,
        "X-RapidAPI-Host": secrets.RAPIDAPI_HOST
    }
    params = {"game": game_id}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    # Optionally save raw data
    with open(f'data/raw/game_{game_id}.json', 'w') as f:
        json.dump(data, f)

    return data
