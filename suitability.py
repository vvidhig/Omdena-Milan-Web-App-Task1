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
        .centered {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .button {{
            font-size: 20px;
            padding: 15px 30px;
        }}
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
    
    # Centered container for buttons
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    # Predict using Supervised Model button
    if st.button("Predict using Supervised Model", key="supervised_model_button", class_="button"):
        prediction = predict_supervised(latitude, longitude)
        st.write("Prediction Result (Supervised Model):")
        if prediction == 0:
            st.error("Not suitable for urban farming")
        elif prediction == 1:
            st.success("Suitable for urban farming")
        else:
            st.error("Invalid prediction result")
    
    # Predict using Unsupervised Model button
    if st.button("Predict using Unsupervised Model", key="unsupervised_model_button", class_="button"):
        prediction = predict_unsupervised(latitude, longitude)
        st.write("Prediction Result (Unsupervised Model):")
        if prediction == 0:
            st.success("Suitable for agriculture")
        elif prediction in [1, 2, 3]:  # Adjust according to your unsupervised model predictions
            st.error("Not suitable for agriculture")
        else:
            st.error("Invalid prediction result")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
