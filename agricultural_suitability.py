# main.py
import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def main_page():    
    st.title("Agriculture Suitability Prediction")
    
    st.write("""
    ### XGBClassifier
    XGBoost is a popular and efficient machine learning algorithm that implements gradient boosting. 
    It is widely used for classification and regression tasks due to its high performance and speed. 
    Our XGBClassifier model is trained to predict the suitability of an area for urban farming based on various features.
    """)
    
    if st.button("Predict using Supervised Model"):
        st.query_params.update({"page": "supervised"})
        st.rerun()
    
    st.write("""
    ### KMeans Model
    KMeans is an unsupervised learning algorithm used for clustering. 
    It partitions the data into K clusters based on feature similarity. 
    Our KMeans model groups areas into clusters to identify patterns in urban farming suitability.
    """)
    
    if st.button("Predict using Unsupervised Model"):
        st.query_params.update({"page": "unsupervised"})
        st.rerun()

def supervised_page():
    import suitability_supervised
    suitability_supervised.app()

def unsupervised_page():
    import suitability_unsupervised
    suitability_unsupervised.app()

def app():
    if "page" in st.query_params:
        if st.query_params["page"] == "supervised":
            supervised_page()
        elif st.query_params["page"] == "unsupervised":
            unsupervised_page()
        else:
            main_page()
    else:
        main_page()

if __name__ == "__main__":
    app()