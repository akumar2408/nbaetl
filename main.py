# main.py
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load
import logging

logging.basicConfig(filename='logs/etl.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("ETL process started")

    # Example game ID
    game_id = 8133

    try:
        # Extraction
        logging.info(f"Extracting data for game {game_id}")
        data = extract(game_id)

        # Transformation
        logging.info("Transforming data")
        df = transform(data)

        # Loading
        logging.info("Loading data into database")
        load(df)

        logging.info("ETL process completed successfully")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    main()
