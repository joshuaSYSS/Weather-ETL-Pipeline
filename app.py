import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("Hong Kong Weather Map")

conn = sqlite3.connect("weather.db")

df = pd.read_sql("SELECT place, value, lat, lon FROM weather_obs", conn)

df["dot_size"] = df["value"] / 20

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    color="value",
    size = "dot_size",              
    hover_name="place",               
    hover_data=["value"],       
    color_continuous_scale="RdYlBu_r",
    size_max=40,
    zoom=9,
    mapbox_style="carto-positron"
)

fig.update_layout(
    height=600, 
    width=1500
)

st.plotly_chart(fig, use_container_width=True)
