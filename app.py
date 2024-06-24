import streamlit as st
from predict import predict

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
        # Make the prediction using the latitude and longitude
        prediction = predict(latitude, longitude)

        # Display the result
        if isinstance(prediction, str):
            st.error(prediction)
        elif prediction == 1:
            st.success("This area is suitable for agriculture.")
        else:
            st.error("This area is not suitable for agriculture.")

if __name__ == "__main__":
    main()
