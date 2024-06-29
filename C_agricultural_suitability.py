import streamlit as st
from C1_predict import run_app as predict_using_all
from C2_predict import app as predict_using_latlong

def main_page():
    col1, col2, col3, col4 = st.columns([1,1,3,1], gap='medium')
    with col1:
        st.page_link(r"A_home.py", label="Home", icon="🏠")
    with col2:
        st.page_link(r"B_eda.py", label="EDA", icon="📶")
    with col3:
        st.page_link(r"C_agricultural_suitability.py", label="Find Suitable Area for Uraban Farming", icon="🤖")
    with col4:
        st.page_link(r"D_contact.py", label="Contact Us", icon="📧")
    
    
    st.title("Agriculture Suitability Prediction")
    
    st.write("""
    ### Predict using all the parameters
    """)
    
    if st.button("Predict using All the Values"):
        st.session_state.page = "supervised"
        st.experimental_rerun()
    
    st.write("""
    ### Predict using only the Latitude and Longitude
    """)
    
    if st.button("Predict using only Latitude and Longitude"):
        st.session_state.page = "unsupervised"
        st.experimental_rerun()

def predict_using_all():
    import  C1_predict
    C1_predict.run_app()

def predict_using_latlong():
    import C2_predict
    C2_predict.app()

def app():
    if 'page' not in st.session_state:
        st.session_state.page = "main"

    if st.session_state.page == "supervised":
        predict_using_all()
    elif st.session_state.page == "unsupervised":
        predict_using_latlong()
    else:
        main_page()

if __name__ == "__main__":
    app()