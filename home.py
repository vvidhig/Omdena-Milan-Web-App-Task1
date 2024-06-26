import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_image():
    image_path = "Images/predict_bg.jpg"
    encoded_image = get_base64_of_bin_file(image_path)
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
    
    st.title("Agriculture Suitability Analysis")
    st.subheader("Welcome to the Agriculture Suitability Analysis Tool")

    st.markdown("""
    This application helps you analyze and visualize the suitability of different areas for agriculture using latitude and longitude inputs. Our powerful machine learning model predicts the agricultural suitability based on various factors.

    ### Features:
    - **Exploratory Data Analysis (EDA)**: Understand the data through visualizations.
    - **Agricultural Suitability Prediction**: Input latitude and longitude to check the suitability of the area for agriculture.
    """)

    st.image("Images/home_page.jpg", caption="Agricultural Land")  # Replace with your image URL

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

