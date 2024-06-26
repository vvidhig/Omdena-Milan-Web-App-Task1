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
    set_background_image
    st.title("about Page")
    st.write("This is the About page.")
    # Add your account page logic here
