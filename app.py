import streamlit as st
import sqlite3
import pandas as pd
from main import run_pipeline

run_pipeline()

st.title("Hong Kong Weather Dashboard")

conn = sqlite3.connect("weather.db")
df = pd.read_sql("SELECT * FROM weather_obs DESC LIMIT 100", conn)

st.write("Latest Weather Data")
st.dataframe(df)

st.line_chart(df[['place', 'value']].set_index('place'))
