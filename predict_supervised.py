import pickle
import numpy as np
import pandas as pd
import streamlit as st
from data_fetcher import DataFetcher

# Load the trained model
with open('models/XGBClassifier_Pipeline_Optuna_Vidhi.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize DataFetcher
data_fetcher = DataFetcher('dataset/Merged_2023.csv')

def predict(latitude, longitude):
    # Fetch additional data based on latitude and longitude
    additional_data = data_fetcher.fetch_data(latitude, longitude)

    if additional_data is None:
        st.error("No data found for the given latitude and longitude.")
    else:
        # Prepare the input data for the model as a Pandas DataFrame
        input_data = pd.DataFrame({
            'Latitude': [latitude],
            'Longitude': [longitude],
            'Zone': [additional_data['Zone']],
            'NDVI': [additional_data['NDVI']],
            'landuse': [additional_data['landuse']],
            'LST': [additional_data['LST']],
            'NDBI': [additional_data['NDBI']],
            'NDWI': [additional_data['NDWI']],
            'Roughness': [additional_data['Roughness']],
            'SAVI': [additional_data['SAVI']],
            'Slope': [additional_data['Slope']],
            'SMI': [additional_data['SMI']],
            'solar_radiation': [additional_data['solar_radiation']]
        })

        # Write the additional features with custom styling
        st.markdown(
            """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Playwrite+DE+Grund:wght@100..400&family=Teko:wght@300..700&display=swap');
            .custom-text {
                font-family: 'Teko', sans-serif;
                font-size: 1.5em;
                color: #556B2F; /* Olive green color */
                font-weight: 500;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.write("### Additional Features:", unsafe_allow_html=True)

        features = [
            ('Zone', f"{additional_data['Zone']}"),
            ('NDVI (Normalized Difference Vegetation Index)', f"{additional_data['NDVI']:.6f}"),
            ('Land Use', f"{additional_data['landuse']}"),
            ('Surface Temperature (LST)', f"{additional_data['LST']:.6f}"),
            ('NDBI (Normalized Difference Built-up Index)', f"{additional_data['NDBI']:.6f}"),
            ('NDWI (Normalized Difference Water Index)', f"{additional_data['NDWI']:.6f}"),
            ('Roughness', f"{additional_data['Roughness']:.6f}"),
            ('SAVI (Soil-Adjusted Vegetation Index)', f"{additional_data['SAVI']:.6f}"),
            ('Land Slope', f"{additional_data['Slope']:.6f}"),
            ('SMI (Soil Moisture)', f"{additional_data['SMI']:.6f}"),
            ('Solar Radiation', f"{additional_data['solar_radiation']:.6f}")
        ]

        cols = st.columns(3)
        for i, (name, value) in enumerate(features):
            cols[i % 3].write(f"<span class='custom-text'>{name}: {value}</span>", unsafe_allow_html=True)

        # Make the prediction
        prediction = model.predict(input_data)

        if prediction[0] == 0:
            st.error("The area is Not Suitable for Urban Farming")
        else:
            st.success("The area is Suitable for Urban Farming")

