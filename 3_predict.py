import streamlit as st
import pickle
import numpy as np

# Load the models (adjust paths as necessary)
with open('models/kmeans_model_pipeline_Sneha.pkl', 'rb') as f:
    supervised_model = pickle.load(f)

with open('models/XGBClassifier_Pipeline_Optuna_Vidhi.pkl', 'rb') as f:
    unsupervised_model = pickle.load(f)

# Function to get prediction
def get_prediction(model, features):
    if isinstance(model, type(supervised_model)):
        return model.predict([features])[0]
    elif isinstance(model, type(unsupervised_model)):
        return model.predict([features])[0]

# Function to display the Streamlit app
def run_app():
    st.title('Urban Farming Suitability Analysis')

    # Input fields arranged in rows of four
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        smi = st.number_input('SMI')
    with col2:
        ndbi = st.number_input('NDBI')
    with col3:
        roughness = st.number_input('Roughness')
    with col4:
        slope = st.number_input('Slope')

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        ndvi = st.number_input('NDVI')
    with col6:
        lst = st.number_input('LST')
    with col7:
        ndwi = st.number_input('NDWI')
    with col8:
        savi = st.number_input('SAVI')

    col9, col10, col11, col12 = st.columns(4)
    with col9:
        landuse = st.selectbox('Landuse', ['Urban', 'Agriculture', 'Forest', 'Water', 'Barren'])
    with col10:
        solar_radiation = st.number_input('Solar Radiation')
    with col11:
        longitude = st.number_input('Longitude')
    with col12:
        latitude = st.number_input('Latitude')

    # Model selection
    model_type = st.selectbox('Select Model', ['Supervised Model : XGBClassifier', 'Unsupervised Model : KmeansClassifier'])

    # Model mapping
    model = supervised_model if model_type == 'Supervised Model' else unsupervised_model

    # Predict button
    if st.button('Predict'):
        features = np.array([
            smi, ndbi, roughness, slope,
            ndvi, lst, ndwi, savi,
            landuse, solar_radiation, longitude, latitude
        ])
        
        prediction = get_prediction(model, features)
        suitability = 'Suitable' if prediction == 1 else 'Not Suitable'
        
        st.write(f'The land is {suitability} for urban farming.')

if __name__ == '__main__':
    run_app()
