import streamlit as st
import pandas as pd

st.title("Mini Verkaufs-Dashboard")

#  Cache: CSV nur einmal laden
@st.cache_data
def lade_daten():
    return pd.read_csv("verkauf.csv")

df = lade_daten()


jahr = st.selectbox("Wähle ein Jahr", df["Jahr"].unique())

df_filtered = df[df["Jahr"] == jahr]


col1, col2 = st.columns(2)

col1.metric("Gesamt-Umsatz", df_filtered["Umsatz"].sum())
col2.metric("Durchschnitt", int(df_filtered["Umsatz"].mean()))

st.dataframe(df_filtered)