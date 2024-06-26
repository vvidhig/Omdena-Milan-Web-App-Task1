import streamlit as st
import pandas as pd
import plotly.express as px

# Function to define EDA for Zone 4 (or any other zone)
def app():
    st.title("EDA Page for Zone 4")
    st.write("This is the EDA page for Zone 4.")
    
    # Load data and perform EDA
    # Replace with your EDA logic specific to Zone 4
    df = pd.read_csv('dataset/Merged_2014.csv')
    
    # Example EDA output
    st.write(df.head())  # Display the first few rows of data
    st.write(df.describe())  # Display summary statistics
    
    # Example Plotly Express chart
    fig = px.histogram(df, x='column_name')
    st.plotly_chart(fig)
