import streamlit as st

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

def app():
    set_background_image()
    
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
