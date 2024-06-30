import streamlit as st

def navbar():
    st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: space-evenly;
        background-color: #333;
        padding: 10px 0;
        margin-bottom: 20px;
    }
    .navbar-item {
        color: white;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 4px;
    }
    .navbar-item:hover {
        background-color: #ddd;
        color: black;
    }
    .navbar-item.active {
        background-color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

    pages = {
        'Home': 'A_home.py',
        'EDA': 'B_eda.py',
        'Agricultural Suitability': 'C_agricultural_suitability.py',
        'Contact': 'D_contact.py'
    }

    st.markdown('<div class="navbar">', unsafe_allow_html=True)
    for page, file in pages.items():
        active = ' active' if st.session_state.page == page else ''
        st.markdown(f'<a class="navbar-item{active}" href="javascript:void(0);" onclick="changePage(\'{page}\')">{page}</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <script>
    function changePage(page) {
        window.parent.postMessage({type: 'streamlit:setComponentValue', value: page}, '*');
    }
    </script>
    """, unsafe_allow_html=True)