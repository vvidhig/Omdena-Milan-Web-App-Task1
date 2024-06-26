import streamlit as st
import pandas as pd
import plotly.express as px

# Function to show Zone 4 dashboard
def show_dashboard_zone9():
    st.title("Zone 9 EDA Dashboard")
    st.write("This is the dashboard for EDA of Zone 9.")
    
    # Load data
    @st.cache(allow_output_mutation=True)
    def load_data():
        df = pd.read_csv('dataset/Merged_2014.csv')
        return df
    
    df = load_data()
    
    # Filter data for Zone 4
    zone_9_df = df[df['Zone'] == 'zone9']
    
    # Numerical features
    numerical_features = ['SMI', 'NDBI', 'Roughness', 'Slope', 'NDVI', 'NDWI', 'SAVI', 'solar_radiation']
    
    # Display data
    st.markdown("### Data Overview")
    st.write(zone_9_df)
    
    # Display summary statistics
    st.markdown("### Summary Statistics for All Numerical Features")
    st.write(zone_9_df[numerical_features].describe())
    
    # Display visualizations for numerical features
    st.markdown("### Visualizations for Numerical Features")
    
    for feature in numerical_features:
        st.markdown(f"#### Analysis of {feature}")
        
        # Histogram
        st.plotly_chart(px.histogram(zone_9_df, x=feature, marginal="box", color_discrete_sequence=px.colors.qualitative.Set3))
        
        # Scatter Plot
        st.plotly_chart(px.scatter(zone_9_df, x='Latitude', y='Longitude', color=feature, color_continuous_scale=px.colors.diverging.Tealrose))
        
        # Line Plot
        st.plotly_chart(px.line(zone_9_df.sort_values(by='Latitude'), x='Latitude', y=feature, color_discrete_sequence=px.colors.qualitative.Set3))
        
        # Bar Chart
        st.plotly_chart(px.bar(zone_9_df, x='Latitude', y=feature, color_discrete_sequence=px.colors.qualitative.Set3))
        
        # Violin Plot
        st.plotly_chart(px.violin(zone_9_df, y=feature, color_discrete_sequence=px.colors.qualitative.Set3))
        
        # Pie Chart
        binned_data = pd.cut(zone_9_df[feature], bins=5).value_counts()
        binned_data.index = binned_data.index.astype(str)  # Convert intervals to string
        st.plotly_chart(px.pie(values=binned_data.values, names=binned_data.index, title=f'{feature} Distribution'))
        
        st.markdown("---")  # Separator between sections
    
    # Correlation Heatmap
    st.markdown("### Correlation Heatmap")
    corr = zone_9_df[numerical_features].corr()
    st.plotly_chart(px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale=px.colors.diverging.Tealrose))