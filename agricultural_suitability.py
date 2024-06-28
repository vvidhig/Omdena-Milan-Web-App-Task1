# main.py
import streamlit as st
import base64

def set_background_image():
    image_path = "Images/predict_bg.jpg"
    with open(image_path, 'rb') as f:
        data = f.read()
    encoded_image = base64.b64encode(data).decode()
    image_css = f"""
        <style>
        body {{
            background-image: url('data:image/jpeg;base64,{encoded_image}');
            background-size: cover;
        }}
        </style>
    """
    st.markdown(image_css, unsafe_allow_html=True)

def main_page():
    set_background_image()
    
    st.title("Agriculture Suitability Prediction")
    
    st.write("""
    ### XGBClassifier
    XGBoost is a popular and efficient machine learning algorithm that implements gradient boosting. 
    It is widely used for classification and regression tasks due to its high performance and speed. 
    Our XGBClassifier model is trained to predict the suitability of an area for urban farming based on various features.
    """)
    
    if st.button("Predict using Supervised Model"):
        st.set_query_params(page="supervised")
        st.experimental_rerun()
    
    st.write("""
    ### KMeans Model
    KMeans is an unsupervised learning algorithm used for clustering. 
    It partitions the data into K clusters based on feature similarity. 
    Our KMeans model groups areas into clusters to identify patterns in urban farming suitability.
    """)
    
    if st.button("Predict using Unsupervised Model"):
        st.set_query_params(page="unsupervised")
        st.experimental_rerun()

def supervised_page():
    import suitability_supervised
    suitability_supervised.app()

def unsupervised_page():
    import suitability_unsupervised
    suitability_unsupervised.app()

def app():
    query_params = st.experimental_get_query_params()
    if "page" in query_params:
        if query_params["page"][0] == "supervised":
            supervised_page()
        elif query_params["page"][0] == "unsupervised":
            unsupervised_page()
        else:
            main_page()
    else:
        main_page()

if __name__ == "__main__":
    app()
