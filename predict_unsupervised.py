import pickle
import numpy as np
import pandas as pd
from data_fetcher import DataFetcher

# Load the trained model
with open('kmeans_model_pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize DataFetcher
# data_fetcher = DataFetcher('dataset/Merged_2014.csv')
data_fetcher = DataFetcher('dataset/MergedData_2023.csv')


def predict_unsupervised(latitude, longitude):
    # Fetch additional data based on latitude and longitude
    additional_data = data_fetcher.fetch_data(latitude, longitude)

    if additional_data is None:
        return "No data found for the given latitude and longitude."

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

    # Make the prediction
    prediction = model.predict(input_data)

    if prediction[0] == 0:
        return "The area is suitable for urban farming"
    else:
        return "The area is not suitable for urban farming"