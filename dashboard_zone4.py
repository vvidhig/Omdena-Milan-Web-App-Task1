import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# Load data
df = pd.read_csv('dataset/Merged_2014.csv')

# Filter data for Zone 4
zone_4_df = df[df['Zone'] == 'zone4']

# Display Zone 4 data
st.title("Dashboard for Zone 4")

# Display data
st.subheader("Data")
st.write(zone_4_df)

# Generate visualizations for numerical features
st.subheader("Visualizations for Numerical Features")

numerical_features = ['SMI', 'NDBI', 'Roughness', 'Slope', 'NDVI', 'LST', 'NDWI', 'SAVI', 'solar_radiation']

for feature in numerical_features:
    st.subheader(f"Analysis of {feature}")

    # Create two columns to place graphs side by side
    col1, col2 = st.columns(2)

    # 1. Histogram (Distplot)
    with col1:
        st.write(f"Histogram of {feature}")
        fig, ax = plt.subplots()
        sns.histplot(data=zone_4_df, x=feature, kde=True, ax=ax)
        st.pyplot(fig)

    # 2. Box Plot
    with col2:
        st.write(f"Box Plot of {feature}")
        fig, ax = plt.subplots()
        sns.boxplot(data=zone_4_df, y=feature, ax=ax)
        st.pyplot(fig)

    st.markdown("---")  # Separator between sections

    # Create another row for additional visualizations if needed

# Overall Summary Statistics
st.subheader("Summary Statistics for All Numerical Features")
st.write(zone_4_df[numerical_features].describe())

# Pairplot
st.subheader("Pairplot of All Numerical Features")
fig = sns.pairplot(zone_4_df[numerical_features], diag_kind='kde')
st.pyplot(fig)
