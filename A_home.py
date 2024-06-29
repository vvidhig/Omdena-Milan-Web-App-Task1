import streamlit as st
def app():
    col1, col2, col3, col4 = st.columns([1,1,3,1], gap='medium')
    with col1:
        st.page_link(r"A_home.py", label="Home", icon="🏠")
    with col2:
        st.page_link(r"B_eda.py", label="EDA", icon="📶")
    with col3:
        st.page_link(r"C_agricultural_suitability.py", label="Find Suitable Area for Uraban Farming", icon="🤖")
    with col4:
        st.page_link(r"D_contact.py", label="Contact Us", icon="📧")
            
    st.title("Agriculture Suitability Analysis")
    st.subheader("Welcome to the Agriculture Suitability Analysis Tool")

    st.markdown("""
    This application helps you analyze and visualize the suitability of different areas for agriculture using latitude and longitude inputs. Our powerful machine learning model predicts the agricultural suitability based on various factors.

    ### Features:
    - **Exploratory Data Analysis (EDA)**: Understand the data through visualizations.
    - **Agricultural Suitability Prediction**: Input latitude and longitude to check the suitability of the area for agriculture.
    """)

    # if st.button("Go to Latitude and Longitude Suitability"):
    #     st.experimental_set_query_params(page="suitability")

    # if st.button("Go to Exploratory Data Analysis (EDA)"):
    #     st.experimental_set_query_params(page="eda")

    # query_params = st.experimental_get_query_params()
    # if "page" in query_params:
    #     page = query_params["page"][0]
    #     if page == "suitability":
    #         st.write("You would now be directed to the Latitude and Longitude Suitability page.")
    #     elif page == "eda":
    #         st.write("You would now be directed to the Exploratory Data Analysis (EDA) page.")

