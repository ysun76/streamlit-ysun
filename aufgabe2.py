import streamlit as st

st.title("Klick-Zähler App")

# ❌ FALSCHER Ansatz (funktioniert nicht richtig!)
# count = 0
# if st.button("Klick mich"):
#     count += 1
# st.write("Zähler:", count)

# ✅ RICHTIGER Ansatz mit session_state
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Klick mich"):
    st.session_state.count += 1

if st.button("Reset"):
    st.session_state.count = 0

st.write("Zähler:", st.session_state.count)