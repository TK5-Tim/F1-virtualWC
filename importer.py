import json
import pandas as pd
import requests
from tqdm import tqdm

base_url= "https://raw.githubusercontent.com/TK5-Tim/F1-virtualWC/tree/master/data/"
season_url = base_url + "season{}/races.json"
quali_url = base_url + "season{}/quali/{}.json"
race_url = base_url + "season{}/race/{}.json"

def parse_season(season_id):
    races = requests.get(url=season_url.format(season_id)).json()
    race_ids = [r['race_id'] for m in races]

    all_drivers = []
    for race_id in tqdm(race_ids):
        race = requests.get(url= race_url.format(season_id, race_id)).json()

def parse_race(race_id,season_id):
    race = requests.get(url= race_url.format(season_id, race_id)).json()
    results = []

    for d in race:
        attributes = {
            "race_id" : race_id,
            "driver_id": d["driver_id"],
            "driver": d["driver_name"],
            "team_id": d["team_id"],
            "team": d["team_name"],
            "race_position": d["race"]["position"],
            "quali_position": d["quali"]["position"],
        }   
        results.append(attributes)
        
    return pd.DataFrame(results)