import os
import streamlit as st
import base64

def app():
    # Set custom font for the title
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playwrite+US+Modern:wght@100..400&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playwrite+DE+Grund:wght@100..400&display=swap');

        .custom-title {
            font-family: 'Playwrite US Modern', sans-serif;
            font-size: 2.5em;
            color: #556B2F; /* Change the color to your preference */
            font-weight: 400;
        }
        .custom-subheader {
            font-family: "Playwrite DE Grund" , sans-serif;
            font-size: 1.4em;
            color: #4CAF50; /* Change the color to your preference */
        }

        .custom-text {
            font-family: "Playwrite DE Grund", sans-serif;
            font-size: 1.2em;
            color: #8B4513; /* Change the color to #8B4513 */
            text-align: justify;
        }
        .feature-list {
            font-family: "Playwrite DE Grund", sans-serif;
            font-size: 1.1em;
            color: #8B4513; /* Change the color to #8B4513 */
        }
        .feature-list h3 {
            color: #800000; /* Change the color of h3 to #800000 */
            font-size: 1.3em;
        }
        .feature-list li {
            margin-bottom: 10px;
        }
        .image-caption {
            font-family: 'Playwrite US Modern', sans-serif;
            font-size: 0.7em;
            color: #E2A76F; /* Change the color to orange */
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<p class="custom-title">Agriculture Suitability Analysis</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-subheader">Welcome to the Agriculture Suitability Analysis Tool</p>', unsafe_allow_html=True)

    # Ensure the correct path to the image
    image_path = os.path.join(os.path.dirname(__file__), 'Images', 'home_page_gif.gif')

    # Add your GIF here with custom caption color
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/gif;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" alt="Agriculture Suitability Analysis" style="width: 100%;">
            <p class="image-caption">Sowing Seeds of Sustainability 🌱</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="custom-text">
        This application helps you analyze and visualize the suitability of different areas for agriculture using latitude and longitude inputs. Our powerful machine learning model predicts the agricultural suitability based on various factors.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="custom-text">
        <h3>Features:</h3>
        <ul class="feature-list">
            <li><b>Exploratory Data Analysis (EDA)</b>: Understand the data through visualizations.</li>
            <li><b>Agricultural Suitability Prediction</b>: Input latitude and longitude to check the suitability of the area for agriculture.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()

