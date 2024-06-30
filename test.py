import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_and_text_color(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .stApp, p, h1, h2, h3, h4, h5, h6 {{
        color: #FCF9DA !important;
    }}
    .stButton > button {{
        background-color: #FFBD59 !important;
        color: #404040 !important;
        border: 1px solid rgba(0,0,0,0.2);
    }}
    .stSlider > div > div > div > div {{
        background-color: rgb(100,152,71) !important;
    }}
    .stSlider > div > div > div > div > div {{
        color: black !important;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Example usage with your background image
set_background_and_text_color('Images/bg.png')

# Example inputs and buttons to see the styling
st.text_input("Enter something:")
st.number_input("Enter a number:")
st.button("Submit")
