import streamlit as st

def app():
    st.title("EDA Page")
    st.write("This is the EDA page.")
    
    # Embed Looker Studio report
    st.markdown("""
    <iframe width="100%" height="600px" src="https://your-looker-studio-embed-url" frameborder="0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

