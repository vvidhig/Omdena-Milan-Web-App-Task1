import streamlit as st
from C1_predict import run_app as predict_using_all
from C2_predict import app as predict_using_latlong

def main_page():
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