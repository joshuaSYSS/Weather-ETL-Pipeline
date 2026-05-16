import pandas as pd

def transform_weather_data(temps):
    df = pd.DataFrame(temps)
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna(subset=['value'])
    return df