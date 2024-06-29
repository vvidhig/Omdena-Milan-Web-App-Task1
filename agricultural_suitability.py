# main.py
import streamlit as st
import base64
def main_page():
    st.title("Agriculture Suitability Prediction")
    
    st.write("""
    ### XGBClassifier
    XGBoost is a popular and efficient machine learning algorithm that implements gradient boosting. 
    It is widely used for classification and regression tasks due to its high performance and speed. 
    Our XGBClassifier model is trained to predict the suitability of an area for urban farming based on various features.
    """)
    
    if st.button("Predict using All the Values"):
        st.session_state.page = "supervised"
        st.experimental_rerun()
    
    st.write("""
    ### KMeans Model
    KMeans is an unsupervised learning algorithm used for clustering. 
    It partitions the data into K clusters based on feature similarity. 
    Our KMeans model groups areas into clusters to identify patterns in urban farming suitability.
    """)
    
    if st.button("Predict using Latitude and Longitude"):
        st.session_state.page = "unsupervised"
        st.experimental_rerun()

def supervised_page():
    import suitability_supervised
    suitability_supervised.app()

def unsupervised_page():
    import suitability_unsupervised
    suitability_unsupervised.app()

def app():
    if 'page' not in st.session_state:
        st.session_state.page = "main"

    if st.session_state.page == "supervised":
        supervised_page()
    elif st.session_state.page == "unsupervised":
        unsupervised_page()
    else:
        main_page()

if __name__ == "__main__":
    app()