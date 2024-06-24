import streamlit as st
import pandas as pd

# Set the title of the web app
st.title("Latitude and Longitude Input App")

# Prompt user for latitude and longitude input
latitude = st.number_input("Enter Latitude:", format="%.6f")
longitude = st.number_input("Enter Longitude:", format="%.6f")

# Display the entered latitude and longitude
st.write("Entered Latitude:", latitude)
st.write("Entered Longitude:", longitude)

# Optionally, you can add a map to visualize the entered location
if st.button("Show on Map"):
    st.map(pd.DataFrame({'lat': [latitude], 'lon': [longitude]}))
