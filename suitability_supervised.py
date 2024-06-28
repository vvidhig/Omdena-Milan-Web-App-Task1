# suitability_supervised.py
import streamlit as st

def app():
    st.title("Supervised Model Prediction")
    st.write("Here, you can add the code to perform the prediction using the XGBClassifier model.")
    
    # Add your prediction code here
    # Example:
    # result = your_prediction_function(input_data)
    # st.write(f"Prediction result: {result}")

    if st.button("Go back"):
        st.session_state.page = "main"
        st.rerun()

if __name__ == "__main__":
    app()