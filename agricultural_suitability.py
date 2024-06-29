# main.py
import streamlit as st
import base64
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