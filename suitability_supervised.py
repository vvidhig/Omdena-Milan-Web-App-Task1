import streamlit as st

def app():
    st.title("Supervised Model Prediction")
    st.write("Here, you can add the code to perform the prediction using the XGBClassifier model.")

    if st.button("Go back"):
        st.set_query_params(page="main")
        st.experimental_rerun()
