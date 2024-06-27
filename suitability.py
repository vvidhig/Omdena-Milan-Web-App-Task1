import streamlit as st
import pandas as pd
import base64
from predict import predict as predict_supervised
from predict_unsupervised import predict_unsupervised
from data_fetcher import DataFetcher
import warnings
warnings.filterwarnings("ignore")

def app():
    st.title("Agriculture Suitability Prediction")
    st.write("This is the Sustainability page.")
    
    st.write("""
    Enter the latitude and longitude to predict whether the area is suitable for agriculture.
    """)
    
    # Use unique keys for latitude and longitude inputs
    latitude = st.number_input("Latitude", format="%.6f", key = "<sort1>")
    longitude = st.number_input("Longitude", format="%.6f", key = "<sort2>")
    
    st.write("Entered Latitude:", latitude)
    st.write("Entered Longitude:", longitude)
    
    map_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
    st.write("Location on Map:")
    st.map(map_data)
    
    if st.button("Predict using Supervised Model"):
        prediction = predict_supervised(latitude, longitude)
    
    if st.button("Predict using Unsupervised Model"):
        prediction = predict_unsupervised(latitude, longitude)

if __name__ == "__main__":
    app()
