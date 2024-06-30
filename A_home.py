import streamlit as st

def app():
    
    st.title("Agriculture Suitability Analysis")
    st.subheader("Welcome to the Agriculture Suitability Analysis Tool")

    # Add your GIF here
    st.image("Images/home_page_gif.gif", caption="Agriculture Suitability Analysis")

    st.markdown("""
    This application helps you analyze and visualize the suitability of different areas for agriculture using latitude and longitude inputs. Our powerful machine learning model predicts the agricultural suitability based on various factors.

    ### Features:
    - **Exploratory Data Analysis (EDA)**: Understand the data through visualizations.
    - **Agricultural Suitability Prediction**: Input latitude and longitude to check the suitability of the area for agriculture.
    """)

if __name__ == "__main__":
    app()