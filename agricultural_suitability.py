import streamlit as st
def app():
    st.title("Agriculture Suitability Prediction")
    
    st.write("""
    ### XGBClassifier
    XGBoost is a popular and efficient machine learning algorithm that implements gradient boosting. 
    It is widely used for classification and regression tasks due to its high performance and speed. 
    Our XGBClassifier model is trained to predict the suitability of an area for urban farming based on various features.
    """)
    
    if st.button("Predict using Supervised Model"):
        st.write("Prediction using XGBClassifier will be performed here.")
    
    st.write("""
    ### KMeans Model
    KMeans is an unsupervised learning algorithm used for clustering. 
    It partitions the data into K clusters based on feature similarity. 
    Our KMeans model groups areas into clusters to identify patterns in urban farming suitability.
    """)
    
    if st.button("Predict using Unsupervised Model"):
        st.write("Prediction using KMeans will be performed here.")

if __name__ == "__main__":
    app()
