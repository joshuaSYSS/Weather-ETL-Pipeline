import sqlite3

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_obs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place TEXT,
    value REAL,
    unit TEXT
)
""")

conn.commit()
conn.close()