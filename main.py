import sqlite3
from extract import extract_weather_data
from transform import transform_weather_data
from load import load_data
import logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    try:
        logging.info("Pipeline run started")
        
        raw_df = extract_weather_data()
        
        logging.info("Data extraction completed successfully.")

        clean_df = transform_weather_data(raw_df)
        
        logging.info("Data transformation completed successfully.")

        load_data(clean_df)
        
        logging.info("Data loading completed successfully.")
        
    except Exception as e:
        logging.error(f"Pipeline run failed: {e}")

if __name__ == "__main__":
    run_pipeline()