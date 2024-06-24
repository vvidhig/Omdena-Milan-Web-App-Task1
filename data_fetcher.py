import streamlit as st
import pickle
import numpy as np
from data_fetcher import DataFetcher

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize DataFetcher
data_fetcher = DataFetcher('data.csv')

# Define the Streamlit app
def main():
    st.title("Agriculture Suitability Prediction")

    st.write("""
    Enter the latitude and longitude to predict whether the area is suitable for agriculture.
    """)

    # Input fields for latitude and longitude
    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number_input("Longitude", format="%.6f")

    if st.button("Predict"):
        # Fetch additional data based on latitude and longitude
        additional_data = data_fetcher.fetch_data(latitude, longitude)

        if additional_data is None:
            st.error("No data found for the given latitude and longitude.")
        else:
            # Prepare the input data
            input_data = np.array([[
                additional_data['Zone'],
                additional_data['NDVI'],
                additional_data['landuse'],
                additional_data['LST'],
                additional_data['NDBI'],
                additional_data['NDWI'],
                additional_data['Roughness'],
                additional_data['SAVI'],
                additional_data['Slope'],
                additional_data['SMI'],
                additional_data['solar_radiation']
            ]])

            # Make the prediction
            prediction = model.predict(input_data)

            # Display the result
            if prediction == 1:
                st.success("This area is suitable for agriculture.")
            else:
                st.error("This area is not suitable for agriculture.")

if __name__ == "__main__":
    main()
