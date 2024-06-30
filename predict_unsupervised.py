import pickle
import numpy as np
import pandas as pd
import streamlit as st
from data_fetcher import DataFetcher

# Load the trained model
with open('models/kmeans_model_pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize DataFetcher
data_fetcher = DataFetcher('dataset/Merged_2023.csv')

def predict_unsupervised(latitude, longitude):
    # Fetch additional data based on latitude and longitude
    additional_data = data_fetcher.fetch_data(latitude, longitude)

    if additional_data is None:
        st.error("No data found for the given latitude and longitude.")
    else:
        # Prepare the input data for the model as a Pandas DataFrame
        input_data = pd.DataFrame({
            'latitude': [latitude],
            'longitude': [longitude],
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

        st.write("### Additional Features:")
        features = [
            ('Zone', f"{additional_data['Zone']}"),
            ('NDVI', f"{additional_data['NDVI']:.6f}"),
            ('Land Use', f"{additional_data['landuse']}"),
            ('LST', f"{additional_data['LST']:.6f}"),
            ('NDBI', f"{additional_data['NDBI']:.6f}"),
            ('NDWI', f"{additional_data['NDWI']:.6f}"),
            ('Roughness', f"{additional_data['Roughness']:.6f}"),
            ('SAVI', f"{additional_data['SAVI']:.6f}"),
            ('Slope', f"{additional_data['Slope']:.6f}"),
            ('SMI', f"{additional_data['SMI']:.6f}"),
            ('Solar Radiation', f"{additional_data['solar_radiation']:.6f}")
        ]

        cols = st.columns(3)
        for i, (name, value) in enumerate(features):
            cols[i % 3].write(f"**{name}:** {value}")

        # Make the prediction
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("The area is Suitable for Urban Farming")
        else:
            st.error("The area is Not Suitable for Urban Farming")
