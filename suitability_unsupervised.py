import streamlit as st

def app():
    st.title("Unsupervised Model Prediction")
        
    if st.button("Go back"):
        st.session_state.page = "main"
        st.rerun()

if __name__ == "__main__":
    app()