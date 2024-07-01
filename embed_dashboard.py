import streamlit as st

st.set_page_config(
    page_title="Embedded Looker Studio Dashboard",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Embedded Looker Studio Dashboard")

# Embed the Looker Studio dashboard
looker_studio_url = "https://lookerstudio.google.com/s/pq1coKZSZOE"

st.components.v1.iframe(looker_studio_url, width=1200, height=800, scrolling=True)
