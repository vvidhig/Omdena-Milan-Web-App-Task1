import streamlit as st
from streamlit_option_menu import option_menu
import base64
import A_home
from C_agricultural_suitability import app as suitability
from D_contact import contact_page as Contacts
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


st.set_page_config(
    page_title="Agriculture Suitability Analysis",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
with st.sidebar:
    selected_page = option_menu(
        menu_title='Navigation',
        options=['Home','EDA Dashboard', 'Agricultural suitability', 'Contacts'],
        icons=['house-fill', 'trophy-fill', 'chat-fill', 'chat-fill', 'info-circle-fill'],
        menu_icon='chat-text-fill',
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": 'black'},
            "icon": {"color": "white", "font-size": "23px"},
            "nav-link": {"color":"white", "font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# Function to load the selected page
def load_page(page):
    if page == "Home":
        A_home.app()
    elif page == "Agricultural suitability":
        suitability()
    elif page == "EDA Dashboard":
        st.write("This page will contain the EDA")
    elif page == "Contacts":
        Contacts()

if __name__ == "__main__":
    load_page(selected_page)
