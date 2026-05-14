import requests
import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Extract ---
# Example HKO open data feed (replace with actual endpoint you want)
url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
response = requests.get(url)
data = response.json()

# Extract temperature readings
temps = data['temperature']['data']  # list of dicts with 'value', 'unit', 'recordTime', 'place'

# --- Step 2: Transform ---
df = pd.DataFrame(temps)
df['recordTime'] = pd.to_datetime(df['recordTime'])
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# Clean missing values
df = df.dropna(subset=['value'])

# Example transformation: daily average temperature
df['date'] = df['recordTime'].dt.date
daily_avg = df.groupby('date')['value'].mean().reset_index()

# --- Step 3: Visualize ---
plt.figure(figsize=(10,5))
plt.plot(daily_avg['date'], daily_avg['value'], marker='o')
plt.title("Daily Average Temperature (°C)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
