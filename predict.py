import pickle
import numpy as np

# Load the trained model
with open('XGBClassifier_Pipeline_Optuna_Vidhi.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(features):
    # Prepare the input data for the model
    input_data = np.array([[
        features['Zone'],
        features['NDVI'],
        features['landuse'],
        features['LST'],
        features['NDBI'],
        features['NDWI'],
        features['Roughness'],
        features['SAVI'],
        features['Slope'],
        features['SMI'],
        features['solar_radiation']
    ]])

    # Make the prediction
    prediction = model.predict(input_data)
    return prediction
