import streamlit as st
import pandas as pd
from predict import predict  # Assuming predict.py is in the same directory as app.py

def main():
    # Set the title of the web app
    st.title("Agriculture Suitability Prediction")

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

# Ensure main function is executed if app.py is run directly
if __name__ == "__main__":
    main()
