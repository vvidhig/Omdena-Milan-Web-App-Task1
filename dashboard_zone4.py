import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk

# Load data
df = pd.read_csv('dataset/Merged_2014.csv')

# Filter data for Zone 4
zone_4_df = df[df['Zone'] == 'zone4']

# Display Zone 4 data
st.title("Dashboard for Zone 4")

# Display data
st.subheader("Data")
st.write(zone_4_df)

# Rename columns for compatibility with Streamlit's map function
zone_4_df = zone_4_df.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})

# Generate maps and histograms for numerical features
numerical_features = ['SMI', 'NDBI', 'Roughness', 'Slope', 'NDVI', 'LST', 'NDWI', 'SAVI', 'solar_radiation']

st.subheader("Numerical Feature Distributions and Map")

for feature in numerical_features:
    col1, col2 = st.columns(2)
    
    with col1:
        chart = alt.Chart(zone_4_df).mark_bar().encode(
            alt.X(feature, bin=True),
            y='count()'
        ).properties(
            title=f"Distribution of {feature}"
        )
        st.altair_chart(chart, use_container_width=True)
    
    with col2:
        st.map(zone_4_df[['latitude', 'longitude']])

# Generate scatter plot for geographical data
st.subheader("Geographical Scatter Plot")
scatter_chart = alt.Chart(zone_4_df).mark_circle(size=60).encode(
    x='longitude',
    y='latitude',
    color='Zone',
    tooltip=['longitude', 'latitude', 'Zone']
).properties(
    title="Geographical Distribution of Data Points"
).interactive()

st.altair_chart(scatter_chart, use_container_width=True)

# Generate Pydeck map for geographical data
st.subheader("Geographical Distribution")
layer = pdk.Layer(
    "ScatterplotLayer",
    data=zone_4_df,
    get_position='[longitude, latitude]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=zone_4_df['latitude'].mean(),
    longitude=zone_4_df['longitude'].mean(),
    zoom=11,
    pitch=50
)

r = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view_state,
    layers=[layer],
    tooltip={"text": "{Zone}"}
)

st.pydeck_chart(r)
