import streamlit as st
import pandas as pd
from predict_supervised import predict as predict_supervised
from predict_unsupervised import predict_unsupervised
from data_fetcher import DataFetcher

def app():
    if st.button("Go back"):
        st.session_state.page = "main"
        st.rerun()
        
    st.title("Predict using Latitude and Longitude")

    st.write("""
    Enter the latitude and longitude to predict whether the area is suitable for agriculture.
    """)
    
    latitude = st.number_input("Latitude", format="%.8f", key = "<sort1>")
    longitude = st.number_input("Longitude", format="%.8f", key = "<sort2>")
    
    st.write("Entered Latitude:", latitude)
    st.write("Entered Longitude:", longitude)
    
    map_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
    st.write("Location on Map:")
    st.map(map_data)
    
    model_type = st.selectbox('Select Model', ['Supervised Model : XGBClassifier', 'Unsupervised Model : KmeansClassifier'])

    if st.button('Predict'):
        if model_type == 'Supervised Model : XGBClassifier':
            prediction = predict_supervised(latitude, longitude)
        else:
            prediction = predict_unsupervised(latitude, longitude)

if __name__ == "__main__":
    app()