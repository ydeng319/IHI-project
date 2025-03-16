import streamlit as st
import pandas as pd
import pydeck as pdk

# Load data
data = pd.read_csv('Outbreak_240817.csv')

# Create a list of country choices from your data
country_choices = ['All Countries'] + sorted(data['country'].unique())

# Convert 'reportingDate' column to datetime
data['reportingDate'] = pd.to_datetime(data['reportingDate'])

# Streamlit application
st.title('2017 Bird Flu Trend Visualization')

#Selection dropdowns 
with st.sidebar.form(key="my_form"):
    selectbox_country = st.selectbox("Choose a country", country_choices)
    # Default date is set to the earliest reporting date
    date_range = st.date_input("Select reporting date range",
                               value=(data['reportingDate'].min(), data['reportingDate'].max()))
    submit_button = st.form_submit_button("Filter Map")

# If form is submitted, use filtered data; otherwise, default to  data.
if submit_button:
    if selectbox_country == 'All Countries':
        filtered_data = data
    else:
        filtered_data = data[data['country'] == selectbox_country]

    # Define start and end dates from the selected date range
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
     
    # Filter data within the selected date range
    filtered_data = filtered_data[(filtered_data['reportingDate'] >= start_date) & (filtered_data['reportingDate'] <= end_date)]
else:
    filtered_data = data

     
# Create a map using the filtered (or full) dataset
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=filtered_data['latitude'].mean(),
        longitude=filtered_data['longitude'].mean(),
        zoom=2,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=filtered_data,
            get_position='[longitude, latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=50000,
            pickable=True
        ),
    ],
))

#Total case count metric
total_observations = data['country'].count()
st.write("Total case observations:", total_observations)        

#Top country table
country_counts = data.groupby('country').size().reset_index(name='new cases')
top_countries = country_counts.sort_values(by='cases', ascending=False).head(3)

#Top dates table - Yijun
date_counts = data.groupby('reportingDate').size().reset_index(name='new cases')
top_dates = date_counts.sort_values(by='observation_counts', ascending=False).head(3)


# Create two columns for side-by-side display
col1, col2 = st.columns(2)

with col1:
    st.header("Countries with most cases")
    html_table = top_countries.to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)
    
with col2:
    st.header("Dates with most new cases")
    html_table = top_dates.to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)




st.write(data)  # Display the data as a table below the map
