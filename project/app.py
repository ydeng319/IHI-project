import streamlit as st
import pandas as pd
import pydeck as pdk

# Load data
data = pd.read_csv('Outbreak_240817.csv')

# Streamlit application
st.title('Disease Trend Visualization')

# Create a map
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=data['latitude'].mean(),
         longitude=data['longitude'].mean(),
         zoom=2,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[longitude, latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=50000,
            pickable=True
         ),
     ],
 ))

st.write(data)  # Display the data as a table below the map
