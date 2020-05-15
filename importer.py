import json
import pandas as pd



def race_info():
    with open('data/season3/races.json') as f: 
        races = json.load(f)
    
def race_results(race):
    with open('data/season3/race/%d.json' % (race)) as f: 
        race = json.load(f)
    df = pd.io.json.json_normalize(race, sep = "_")
    print(df)

def quali_results(race):
    with open('data/season3/quali/%d.json' % (race)) as f: 
        race = json.load(f)
    print(race)

def race_frame(race): 
    with open('data/season3/races.json') as f: 
        races = json.load(f)
    with open('data/season3/race/%d.json' % (race)) as f: 
        raceData = json.load(f)
    