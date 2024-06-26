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

# Generate scatter plot for geographical data with colored points
st.subheader("Geographical Distribution")
layer = pdk.Layer(
    "ScatterplotLayer",
    data=zone_4_df,
    get_position='[longitude, latitude]',
    get_color='[SMI * 255, NDBI * 255, Roughness * 255, Slope * 255]',  # Adjust colors based on numerical values
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

# Generate histograms for numerical features
st.subheader("Numerical Feature Distributions")

for feature in ['SMI', 'NDBI', 'Roughness', 'Slope', 'NDVI', 'LST', 'NDWI', 'SAVI', 'solar_radiation']:
    chart = alt.Chart(zone_4_df).mark_bar().encode(
        alt.X(feature, bin=True),
        y='count()',
        color=alt.Color(feature, scale=alt.Scale(scheme='viridis'))  # Color bars based on feature value
    ).properties(
        title=f"Distribution of {feature}"
    )
    st.altair_chart(chart, use_container_width=True)
