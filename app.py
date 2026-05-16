import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("Hong Kong Weather Map")

conn = sqlite3.connect("weather.db")

df = pd.read_sql("SELECT place, temperature, lat, lon FROM weather_obs", conn)

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    color="temperature",              
    hover_name="place",               
    hover_data=["temperature"],       
    color_continuous_scale="RdYlBu_r",
    size_max=15,
    zoom=10,
    mapbox_style="carto-positron"     # clean background map
)

st.plotly_chart(fig, use_container_width=True)
