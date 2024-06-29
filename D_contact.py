import streamlit as st


# Function for Contact/Contributors/References/License Page
def contact_page():
    
    col1, col2, col3, col4 = st.columns([1,1,3,1], gap='medium')
    with col1:
        st.page_link(r"A_home.py", label="Home", icon="🏠")
    with col2:
        st.page_link(r"B_eda.py", label="EDA", icon="📶")
    with col3:
        st.page_link(r"C_agricultural_suitability.py", label="Find Suitable Area for Uraban Farming", icon="🤖")
    with col4:
        st.page_link(r"D_contact.py", label="Contact Us", icon="📧")

    st.title("Contact and Contributors")

    st.write("""
    ### Contributors
    - **John Doe** - Data Scientist
    - **Jane Smith** - Environmental Engineer
    - **Alice Johnson** - GIS Specialist

    ### References
    - [Urban Farming Research Paper 1](https://example.com)
    - [Urban Farming Research Paper 2](https://example.com)

    ### License
    This project is licensed under the MIT License. See the [LICENSE](https://example.com) file for details.

    ### Contact
    For any inquiries, please contact us at [email@example.com](mailto:email@example.com).
    """)

if __name__ == "__main__":
    contact_page()