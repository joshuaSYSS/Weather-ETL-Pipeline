import pandas as pd

def transform_weather_data(temps, locations):
    df = pd.DataFrame(temps)
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna(subset=['value'])
    locations_df = pd.DataFrame([
    {"place": name, "lat": coords["lat"], "lon": coords["lon"]}
    for name, coords in locations.items()
    ])
    df = df.merge(locations_df, left_on='place', right_on='place', how='left')
    print(df)
    return df