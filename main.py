import streamlit as st
from streamlit_option_menu import option_menu
import home
import suitability
import eda
import about
import base64

# Function to convert image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to embed base64 image in CSS
def set_background_image():
    image_path = "D:/Heritage Institute of Technology,Kolkata/Omdena/Omdena-Milan-Web-App/image/img2.jpeg"
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


st.set_page_config(
    page_title="Agriculture Suitability Analysis",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="expanded"
)

set_background_image()

# Sidebar navigation
with st.sidebar:
    selected_page = option_menu(
        menu_title='Navigation',
        options=['Home', 'Agricultural suitability', 'EDA', 'About'],
        icons=['house-fill', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
        menu_icon='chat-text-fill',
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": 'black'},
            "icon": {"color": "white", "font-size": "23px"},
            "nav-link": {"color":"white", "font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# Function to navigate to the selected page
def load_page(page):
    if page == "Home":
        home.app()
    elif page == "Agricultural suitability":
        suitability.app()
    elif page == "EDA":
        eda.app()
    elif page == "About":
        about.app()

# Load the selected page
load_page(selected_page)

