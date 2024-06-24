import pickle
import numpy as np
from data_fetcher import DataFetcher

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize DataFetcher
data_fetcher = DataFetcher('data.csv')

def predict(latitude, longitude):
    # Fetch additional data based on latitude and longitude
    additional_data = data_fetcher.fetch_data(latitude, longitude)

    if additional_data is None:
        return "No data found for the given latitude and longitude."

    # Prepare the input data for the model
    input_data = np.array([[
        latitude,
        longitude,
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
    return prediction[0]
