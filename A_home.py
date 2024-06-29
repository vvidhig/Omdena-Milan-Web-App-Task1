import streamlit as st
def app():
        
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

