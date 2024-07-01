import streamlit as st
import matplotlib.pyplot as plt
import os
import base64


# Function for EDA/Dashboards/Features Used Page
def eda_page():
    
    # col1, col2, col3, col4 = st.columns([1,1,3,1], gap='medium')
    # with col1:
    #     st.page_link(r"A_home.py", label="Home", icon="🏠")
    # with col2:
    #     st.page_link(r"B_eda.py", label="EDA", icon="📶")
    # with col3:
    #     st.page_link(r"C_agricultural_suitability.py", label="Find Suitable Area for Uraban Farming", icon="🤖")
    # with col4:
    #     st.page_link(r"D_contact.py", label="Contact Us", icon="📧")

    # st.set_page_config(page_icon=':bar_chart:')
    # st.title("Exploratory Data Analysis")
    # st.header("Feature Distributions and Data Sources")

    # st.write("Here are the features used in the model along with their distributions:")

    # Data to simulate EDA

    # Display distributions of each feature
    
    st.write("""
    Data was collected from various sources such as satellite imagery, geographical surveys, and climate databases.
    Techniques used include remote sensing, GIS analysis, and environmental monitoring.
    """)

    image_path = os.path.join(os.path.dirname(__file__), 'Images', '68586599-1f68-46e1-a3bc-c054c4f40a50.jpeg')

    # Add your GIF here with custom caption color
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/gif;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" alt="Agriculture Suitability Analysis" style="width: 100%;">
            <p class="image-caption">EDA 🌱</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    eda_page()