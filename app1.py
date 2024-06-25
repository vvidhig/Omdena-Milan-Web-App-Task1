import streamlit as st
import pandas as pd
import base64
from predict import predict  # Assuming predict.py is in the same directory as app.py

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get the base64 string of the image
background_image = get_base64("Images/predict_bg.jpg")

custom_css = f"""
<style>
.stApp {{
  background-image: url("data:image/jpg;base64,{background_image}");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}}
.stApp::before {{
  content: "";
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/jpg;base64,{background_image}");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  filter: blur(5px);
  -webkit-filter: blur(5px);
  z-index: -1;
}}

.widget-container {{
  background-color: beige;  /* Ensure beige color is set */
  padding: 20px;
  border-radius: 10px;
  max-width: 800px;
  margin: auto;
  opacity: 1;  /* Set opacity to 1 for full visibility */
  z-index: 1;
  position: relative;
  display: block !important;
  visibility: visible !important;
}}

.stTextInput > div > div > input {{
  background-color: white;
  color: black;
}}

.stButton>button {{
  color: white;
  background-color: green;
  width: 100%;
}}

.stTitle, .stHeader {{
  color: darkgreen;
}}
</style>
"""

# Inject the custom CSS with the background image
st.markdown(custom_css, unsafe_allow_html=True)

# Set the title of the web app
st.title("Agriculture Suitability Prediction")

# Widget container covering the whole input and output section
with st.container():
    st.markdown('<div class="widget-container">', unsafe_allow_html=True)

    # Introduction and user instructions
    st.write("""
    Enter the latitude and longitude to predict whether the area is suitable for agriculture.
    """)

    # Input fields for latitude and longitude
    col1, col2 = st.columns(2)
    with col1:
        latitude = st.number_input("Latitude", format="%.6f")
    with col2:
        longitude = st.number_input("Longitude", format="%.6f")

    # Display the entered latitude and longitude (optional)
    st.write("Entered Latitude:", latitude)
    st.write("Entered Longitude:", longitude)

    # Map to visualize the entered location
    map_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
    st.write("Location on Map:")
    st.map(map_data)

    # Prediction button
    if st.button("Predict"):
        # Make the prediction using the latitude and longitude
        prediction = predict(latitude, longitude)

        # Display the result
        st.write("Prediction Result:")
        if isinstance(prediction, str):
            st.error(prediction)
        elif prediction == 1:
            st.success("This area is suitable for agriculture.")
        else:
            st.error("This area is not suitable for agriculture.")

    st.markdown('</div>', unsafe_allow_html=True)
