import pandas as pd
import logging

def get_excel_data():
    try:
        file_path = 'data/bible_app.xlsx'
        logging.info(f"Attempting to read Excel file from {file_path}")
        df = pd.read_excel(file_path)
        df = df.sort_values(by='ID', ascending=False)
        data = df.to_dict(orient='records')
        logging.info("Successfully read and processed Excel file")
        return data
    except Exception as e:
        logging.error(f"Error reading Excel file: {e}", exc_info=True)
        raise