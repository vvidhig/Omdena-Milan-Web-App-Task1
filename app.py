import streamlit as st
from data_fetcher import DataFetcher
from predict import predict

# Initialize DataFetcher
data_fetcher = DataFetcher('dataset/Merged_2014.csv')

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
            # Make the prediction using the additional data
            prediction = predict(additional_data)

            # Display the result
            if prediction == 1:
                st.success("This area is suitable for agriculture.")
            else:
                st.error("This area is not suitable for agriculture.")

if __name__ == "__main__":
    main()
