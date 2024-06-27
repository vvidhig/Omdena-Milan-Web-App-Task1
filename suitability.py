import streamlit as st
import pandas as pd
import base64
from predict import predict as predict_supervised
from predict_unsupervised import predict_unsupervised
from data_fetcher import DataFetcher

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_image():
    image_path = "Images/predict_bg.jpg"
    encoded_image = get_base64_of_bin_file(image_path)
    image_css = f"""
        <style>
        body {{
            background-image: url('data:image/jpeg;base64,{encoded_image}');
            background-size: cover;
        }}
        </style>
    """
    st.markdown(image_css, unsafe_allow_html=True)

def app():
    set_background_image()
    st.title("Agriculture Suitability Prediction")
    st.write("This is the Sustainability page.")
    
    st.write("""
    Enter the latitude and longitude to predict whether the area is suitable for agriculture.
    """)
    
    latitude = st.number_input("Latitude", format="%.6f", key="suitability_latitude_input")
    longitude = st.number_input("Longitude", format="%.6f", key="suitability_longitude_input")
    
    st.write("Entered Latitude:", latitude)
    st.write("Entered Longitude:", longitude)
    
    map_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
    st.write("Location on Map:")
    st.map(map_data)
    
    if st.button("Predict using Supervised Model"):
        prediction = predict_supervised(latitude, longitude)
        st.write("Prediction Result (Supervised Model):")
        st.write(prediction)
    
    if st.button("Predict using Unsupervised Model"):
        prediction = predict_unsupervised(latitude, longitude)
        st.write("Prediction Result (Unsupervised Model):")
        st.write(prediction)

if __name__ == "__main__":
    app()
