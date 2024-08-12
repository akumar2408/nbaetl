# scripts/transform.py
import pandas as pd

def transform(data):
    df = pd.json_normalize(data['response'])
    df_filtered = df[['player.firstname', 'player.lastname', 'points', 'assists', 'rebounds']]
    
    # Optionally save transformed data
    df_filtered.to_csv('data/processed/transformed_data.csv', index=False)
    
    return df_filtered
