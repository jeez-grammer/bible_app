import pandas as pd

def get_excel_data():
    df = pd.read_excel('data/bible_app.xlsx')
    df = df.sort_values(by='ID', ascending=False) 
    data = df.to_dict(orient='records')
    return data