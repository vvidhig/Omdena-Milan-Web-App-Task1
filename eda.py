import streamlit as st

def app():
    st.title("EDA Page")
    st.write("This is the EDA page.")
    
    # Embed Looker Studio report
    st.markdown("""
    <iframe width="100%" height="600px" src="https://your-looker-studio-embed-url" frameborder="0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
    
    # Centered buttons for EDA of Zone 4 and Zone 9
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("EDA of Zone 4"):
            # Add your action for Zone 4 EDA here
            st.write("Clicked EDA of Zone 4 button")
    
    with col2:
        if st.button("EDA of Zone 9"):
            # Add your action for Zone 9 EDA here
            st.write("Clicked EDA of Zone 9 button")

# Run the app
if __name__ == "__main__":
    app()
