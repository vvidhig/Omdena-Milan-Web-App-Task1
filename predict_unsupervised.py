import pickle
import numpy as np
import pandas as pd
import streamlit as st
from data_fetcher import DataFetcher

# Load the trained model
with open('kmeans_model_pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize DataFetcher
data_fetcher = DataFetcher('dataset/MergedData_2023.csv')

def predict_unsupervised(latitude, longitude):
    # Fetch additional data based on latitude and longitude
    additional_data = data_fetcher.fetch_data(latitude, longitude)

    if additional_data is None:
        st.error("No data found for the given latitude and longitude.")
    else:
        # Prepare the input data for the model as a Pandas DataFrame
        input_data = pd.DataFrame({
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
            ('Zone', additional_data['Zone']),
            ('NDVI', additional_data['NDVI']),
            ('Land Use', additional_data['landuse']),
            ('LST', additional_data['LST']),
            ('NDBI', additional_data['NDBI']),
            ('NDWI', additional_data['NDWI']),
            ('Roughness', additional_data['Roughness']),
            ('SAVI', additional_data['SAVI']),
            ('Slope', additional_data['Slope']),
            ('SMI', additional_data['SMI']),
            ('Solar Radiation', additional_data['solar_radiation'])
        ]

        cols = st.columns(3)
        for i, (name, value) in enumerate(features):
            cols[i % 3].metric(label=name, value=value)

        # Make the prediction
        prediction = model.predict(input_data)

        if prediction[0] == 0:
            st.success("The area is Suitable for Urban Farming", unsafe_allow_html=True)
        else:
            st.error("The area is Not Suitable for Urban Farming", unsafe_allow_html=True)
