# scripts/load.py
from sqlalchemy import create_engine
from config import config

def load(df):
    engine = create_engine(config.DB_CONNECTION_STRING)
    df.to_sql('player_stats', engine, if_exists='replace', index=False)
