import streamlit as st

st.title("YsunApp")

name = st.text_input("Bitte gib deinen Namen ein:")
zahl = st.slider("Wähle eine Zahl als dein Alter", 0, 100)

# Streamlit führt das Skript bei jeder Benutzerinteraktion neu aus (z.B. wenn ein Widget geändert wird)

if zahl >= 18:
    st.write(f"Hallo {name}, du bist eine erwachsene Person!")
else:
    st.write(f"Hallo {name}, du bist noch nicht erwachsen!")