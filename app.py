import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

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
        # Prepare the input data
        input_data = np.array([[latitude, longitude]])
        
        # Make the prediction
        prediction = model.predict(input_data)
        
        # Display the result
        if prediction == 1:
            st.success("This area is suitable for agriculture.")
        else:
            st.error("This area is not suitable for agriculture.")
    
if __name__ == "__main__":
    main()
