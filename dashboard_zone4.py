import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import altair as alt

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
numerical_features = ['SMI', 'NDBI', 'Roughness', 'Slope', 'NDVI', 'NDWI', 'SAVI', 'solar_radiation']

# Display Zone 4 data
st.markdown('<p class="big-font">Dashboard for Zone 4</p>', unsafe_allow_html=True)

# Display data
st.markdown('<p class="medium-font">Data Overview</p>', unsafe_allow_html=True)
st.write(zone_4_df, unsafe_allow_html=True)

# Overall Summary Statistics
st.markdown('<p class="medium-font">Summary Statistics for All Numerical Features</p>', unsafe_allow_html=True)
st.write(zone_4_df[numerical_features].describe())

# Generate visualizations for numerical features
st.markdown('<p class="medium-font">Visualizations for Numerical Features</p>', unsafe_allow_html=True)

for feature in numerical_features:
    st.markdown(f'<p class="medium-font">Analysis of {feature}</p>', unsafe_allow_html=True)

    # Create columns to place graphs side by side
    col1, col2, col3 = st.columns(3)

    # Histogram
    with col1:
        st.write(f"Histogram of {feature}")
        fig = px.histogram(zone_4_df, x=feature, marginal="box", color_discrete_sequence=[px.colors.qualitative.Set3[0]])
        st.plotly_chart(fig, use_container_width=True)

    # Box Plot
    with col2:
        st.write(f"Box Plot of {feature}")
        fig = px.box(zone_4_df, y=feature, color_discrete_sequence=[px.colors.qualitative.Set3[1]])
        st.plotly_chart(fig, use_container_width=True)

    # Scatter Plot
    with col3:
        st.write(f"Scatter Plot of {feature}")
        fig = px.scatter(zone_4_df, x='Latitude', y='Longitude', color=feature, color_continuous_scale=px.colors.diverging.Tealrose)
        st.plotly_chart(fig, use_container_width=True)

    # Line Plot
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"Line Plot of {feature}")
        fig = px.line(zone_4_df.sort_values(by='Latitude'), x='Latitude', y=feature, color_discrete_sequence=[px.colors.qualitative.Set3[2]])
        st.plotly_chart(fig, use_container_width=True)

    # Bar Chart
    with col2:
        st.write(f"Bar Chart of {feature}")
        fig = px.bar(zone_4_df, x='Latitude', y=feature, color_discrete_sequence=[px.colors.qualitative.Set3[3]])
        st.plotly_chart(fig, use_container_width=True)

    # Violin Plot
    with col3:
        st.write(f"Violin Plot of {feature}")
        fig = px.violin(zone_4_df, y=feature, color_discrete_sequence=[px.colors.qualitative.Set3[4]])
        st.plotly_chart(fig, use_container_width=True)

    # Heat Map (Only for correlation with other features)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"Heat Map of {feature} Correlation")
        corr = zone_4_df[numerical_features].corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale=px.colors.diverging.Tealrose)
        st.plotly_chart(fig, use_container_width=True)

    # Pie Chart
    with col2:
        st.write(f"Pie Chart of {feature}")
        binned_data = pd.cut(zone_4_df[feature], bins=5).value_counts()
        binned_data.index = binned_data.index.astype(str)  # Convert intervals to string
        fig = px.pie(values=binned_data.values, names=binned_data.index, title=f'{feature} Distribution')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")  # Separator between sections

# Correlation Heatmap
st.markdown('<p class="medium-font">Correlation Heatmap</p>', unsafe_allow_html=True)
corr = zone_4_df[numerical_features].corr()
fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale=px.colors.diverging.Tealrose)
st.plotly_chart(fig, use_container_width=True)

# 3D Scatter Plot
st.markdown('<p class="medium-font">3D Scatter Plot</p>', unsafe_allow_html=True)
fig = px.scatter_3d(zone_4_df, x='SMI', y='NDVI', z='LST', color='solar_radiation', color_continuous_scale=px.colors.diverging.Tealrose)
st.plotly_chart(fig, use_container_width=True)

