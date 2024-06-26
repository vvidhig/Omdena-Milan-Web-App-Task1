import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(layout="wide", page_title="Zone 4 Dashboard")

# Custom CSS to improve appearance
st.markdown("""
<style>
body {
    background-color: white;
    color: black;
}
.big-font {
    font-size:30px !important;
    font-weight: bold;
    text-align: center;
    font-family: 'Arial', sans-serif;
}
.medium-font {
    font-size:24px !important;
    font-weight: bold;
    text-align: center;
    font-family: 'Arial', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset/Merged_2014.csv')
    return df

df = load_data()

# Filter data for Zone 4
zone_4_df = df[df['Zone'] == 'zone4']

# Numerical features
numerical_features = ['SMI', 'NDBI', 'Roughness', 'Slope', 'NDVI', 'LST', 'NDWI', 'SAVI', 'solar_radiation']

# Display Zone 4 data
st.markdown('<p class="big-font">Dashboard for Zone 4</p>', unsafe_allow_html=True)

# Display data
st.markdown('<p class="medium-font">Data Overview</p>', unsafe_allow_html=True)
st.write(zone_4_df)

# Generate visualizations for numerical features
st.markdown('<p class="medium-font">Visualizations for Numerical Features</p>', unsafe_allow_html=True)

for feature in numerical_features:
    st.markdown(f'<p class="medium-font">Analysis of {feature}</p>', unsafe_allow_html=True)

    # Create two columns to place graphs side by side
    col1, col2 = st.columns(2)

    # 1. Histogram (Distplot)
    with col1:
        st.write(f"Histogram of {feature}")
        fig = px.histogram(zone_4_df, x=feature, marginal="box", color_discrete_sequence=[px.colors.qualitative.Set3[0]])
        st.plotly_chart(fig, use_container_width=True)

    # 2. Scatter Plot
    with col2:
        st.write(f"Scatter Plot of {feature}")
        fig = px.scatter(zone_4_df, x='Latitude', y='Longitude', color=feature, color_continuous_scale=px.colors.diverging.Tealrose, title=f'{feature} Scatter Plot')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")  # Separator between sections

# Overall Summary Statistics
st.markdown('<p class="medium-font">Summary Statistics for All Numerical Features</p>', unsafe_allow_html=True)
st.write(zone_4_df[numerical_features].describe())

# Correlation Heatmap
st.markdown('<p class="medium-font">Correlation Heatmap</p>', unsafe_allow_html=True)
corr = zone_4_df[numerical_features].corr()
fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale=px.colors.diverging.Tealrose)
st.plotly_chart(fig, use_container_width=True)

# 3D Scatter Plot
st.markdown('<p class="medium-font">3D Scatter Plot</p>', unsafe_allow_html=True)
fig = px.scatter_3d(zone_4_df, x='SMI', y='NDVI', z='LST', color='solar_radiation', color_continuous_scale=px.colors.diverging.Tealrose)
st.plotly_chart(fig, use_container_width=True)

# Parallel Coordinates Plot
st.markdown('<p class="medium-font">Parallel Coordinates Plot</p>', unsafe_allow_html=True)
fig = px.parallel_coordinates(zone_4_df, color="solar_radiation", labels=numerical_features, color_continuous_scale=px.colors.diverging.Tealrose)
st.plotly_chart(fig, use_container_width=True)
