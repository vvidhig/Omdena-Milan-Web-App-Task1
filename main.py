import streamlit as st
from streamlit_option_menu import option_menu
import base64
import A_home as A_home
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

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_and_text_color(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("data:image/png;base64,%s");
        background-size: 100vw 100vh;
        background-position: center;
        background-repeat: no-repeat;
    }
    body, .stApp, p, h1, h2, h3, h4, h5, h6 {
        color: black !important;
    }
    .stTextInput > div > div > input, 
    .stButton > button,
    .stNumberInputContainer > div > div > div > button {
        background-color: rgb(100,152,71) !important;
        color: black !important;
        border: 1px solid rgba(0,0,0,0.2);
    }
    .stSlider > div > div > div > div {
        background-color: rgb(100,152,71) !important;
    }
    .stSlider > div > div > div > div > div {
        color: black !important;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Example usage with your background image
set_background_and_text_color('Images/bg.png')

# Horizontal navbar
selected_page = option_menu(
    menu_title=None,
    options=['Home', 'EDA Dashboard', 'Check Suitable Areas', 'Contacts and Contributors'],
    icons=['house-fill', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
    styles={
        "container": {
            "padding": "0!important", 
            "background-color": "#A5D97E",
            "width": "100%",  # Makes the navbar full width
            "margin": "0 auto",  # Centers the navbar
            "text-align": "center",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
        },
        "icon": {"color": "black", "font-size": "17px"},  # Increased icon size
        "nav-link": {
            "font-size": "17px",
            "text-align": "center",
            "margin": "0px",
            "padding": "7px 7px",  # Increased padding for larger buttons
            "--hover-color": "#71A75E",
            "color": "black",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
        },
        "nav-link-selected": {"background-color": "rgb(100,152,71)"},
    }
)
# Sidebar navigation
# with st.sidebar:
#     sidebar_selected1 = option_menu(
#         menu_title='Navigation',
#         options=['Home','EDA Dashboard', 'Find Suitable Area of Urban Farming', 'Contacts'],
#         icons=['house-fill', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
#         menu_icon='chat-text-fill',
#         default_index=0,
#         styles={
#             "container": {"padding": "5!important", "background-color": '#A5D97E'},
#             "icon": {"color": "black", "font-size": "20px"},
#             "nav-link": {"color":"black", "font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#71A75E"},
#             "nav-link-selected": {"background-color": "#71A75E"},
#             "menu-title": {"color": "black"},
#             "menu-icon": {"color": "black"}
#         }
#     )

# Function to load the selected page
def load_page(page):
    if page == "Home":
        A_home.app()
    elif page == "Check Suitable Areas" or page == "Find Suitable Area of Urban Farming":
        suitability()
    elif page == "EDA Dashboard":
        st.write("This page will contain the EDA")
    elif page == "Contacts and Contributors":
        Contacts()

if __name__ == "__main__":
    page_to_load = selected_page
    load_page(page_to_load)
    # load_page(sidebar_selected1)