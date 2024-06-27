import streamlit as st
import pandas as pd
from predict import predict  # Assuming predict.py is in the same directory as sustainability.py
import base64

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

def predict_unsupervised(latitude, longitude):
    # Replace with your unsupervised model prediction logic
    return "Unsupervised model prediction placeholder."

def predict_supervised(latitude, longitude):
    # Replace with your supervised model prediction logic
    return "Supervised model prediction placeholder."

def app():
    set_background_image()
    st.title("Agriculture Suitability Prediction")
    st.write("This is the Sustainability page.")
    
    # Introduction and user instructions
    st.write("""
    Enter the latitude and longitude to predict whether the area is suitable for agriculture.
    """)
    
    # Input fields for latitude and longitude
    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number_input("Longitude", format="%.6f")
    
    # Display the entered latitude and longitude (optional)
    st.write("Entered Latitude:", latitude)
    st.write("Entered Longitude:", longitude)
    
    # Optionally, you can add a map to visualize the entered location
    map_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
    st.write("Location on Map:")
    st.map(map_data)
    
    # Prediction button (original)
    if st.button("Predict using Supervised Model"):
        prediction = predict(latitude, longitude)
        st.write("Prediction Result:")
        if isinstance(prediction, str):
            st.error(prediction)
        elif prediction == 1:
            st.success("This area is suitable for agriculture.")
        else:
            st.error("This area is not suitable for agriculture.")
    
    
    # Predict using supervised model button
    if st.button("Predict using Unsupervised Model"):
        prediction = predict_supervised(latitude, longitude)
        st.write("Prediction Result (Supervised Model):")
        st.write(prediction)




