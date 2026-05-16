import sqlite3

def load_data(df):
    conn = sqlite3.connect("weather.db")
    df.to_sql("weather_obs", conn, if_exists="replace", index=False)
    conn.close()