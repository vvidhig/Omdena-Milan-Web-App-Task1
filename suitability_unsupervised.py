import streamlit as st

def app():
    st.title("Unsupervised Model Prediction")
    st.write("Here, you can add the code to perform the prediction using the KMeans model.")

    if st.button("Go back"):
        st.experimental_set_query_params(page="main")
        st.experimental_rerun()
