import pandas as pd
import logging

def get_excel_data():
    try:
        file_path = 'data/bible_app.xlsx'
        df = pd.read_excel(file_path)
        df = df.sort_values(by='ID', ascending=False)
        data = df.to_dict(orient='records')
        return data
    except Exception as e:
        logging.error(f"Error reading Excel file: {e}", exc_info=True)
        raise