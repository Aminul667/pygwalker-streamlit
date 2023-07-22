import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

df = pd.read_csv("app/data/airbnb.csv")

print(df.head())
