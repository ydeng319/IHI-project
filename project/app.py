import streamlit as st
import pandas as pd
import pydeck as pdk
import datetime
from google import genai
import os
api_key = os.getenv("GOOGLE_GENAI_API_KEY")
def generate_json(pivot_table):
    output = {}
    for id, row in pivot_table.iterrows():
        output[id] = row['Id']
    return output
def summarize_data(df):
    # Convert 'reportingDate' to datetime
    df['reportingDate'] = pd.to_datetime(df['reportingDate'])

    # Create a 'reportingMonth' column for pivot table
    df['reportingMonth'] = df['reportingDate'].dt.month

    # Pivot table for Number of Observations vs Reporting Month
    pivot_month = pd.pivot_table(df, values='Id', index='reportingMonth', aggfunc='count')
    json_month = generate_json(pivot_month)
    # Pivot table for Number of Observations vs Admin1
    pivot_admin1 = pd.pivot_table(df, values='Id', index='admin1', aggfunc='count')
    json_location = generate_json(pivot_admin1)
    # Pivot table for Number of Observations vs Species Description
    pivot_species = pd.pivot_table(df, values='Id', index='speciesDescription', aggfunc='count')
    json_description = generate_json(pivot_species)
    # return the pivot tables
    return json_month, json_location, json_description
    
def generate_prompt(json_month, json_location, json_description):

    prompt = (
        f"Summarize the bird flu outbreak data from the provided json files. "
        f"The monthly reported cases summary is {json_month}. The reported cases location summary is {json_location}. The reported cases descriptions are summarized as {json_description}.Trends show a "
        f"fluctuation in case numbers across different time periods and regions. "
        "Provide a concise overview of the situation based on these insights within five sentences,."
    )
    return prompt

# Load data
data = pd.read_csv('Outbreak_240817.csv',encoding='ISO-8859-1')

# Create a list of country choices from your data
country_choices = ['All Countries'] + sorted(data['country'].unique())

# Convert 'reportingDate' column to datetime
data['reportingDate'] = pd.to_datetime(data['reportingDate'])

# Streamlit application
st.title('2017 Bird Flu Trend Visualization')
# add llm module
st.header("AI Summary")
# Button to trigger the summary generation
# ai_submit_button = st.button("Generate Summary")

# Placeholder to show the summary
summary_placeholder = st.empty()

# # create prompt
# if ai_submit_button:
#     if genai_trigger == 0:
#         summary_placeholder.markdown("Selected data doesn't exist")
#     else:
#         client = genai.Client(api_key=api_key)
#         response = client.models.generate_content(
#         model="gemini-2.0-flash", contents= generate_prompt(table1, table2, table3))
#         summary_placeholder.markdown(f"**Summary:**\n{response.text}")
#Selection dropdowns 
with st.sidebar.form(key="my_form"):
    selectbox_country = st.selectbox("Choose a country", country_choices)
    # Default date is set to the earliest reporting date
    date_range = st.date_input("Select reporting date range",
                               value =(datetime.date(2015,1,9),
                                       datetime.date(2017, 12, 7)),
                               min_value= datetime.date(2015,1,9),
                               max_value=datetime.date(2017,12,7))
                            #    value=(data['reportingDate'].min(), data['reportingDate'].max())
    submit_button = st.form_submit_button("Filter Map and Summarize Data")

if selectbox_country == 'All Countries':
    filtered_data = data
else:
    filtered_data = data[data['country'] == selectbox_country]

# Convert selected dates to datetime and then to "mm/dd/yyyy" strings for display
start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[1])
start_date_str = start_date.strftime("%m/%d/%Y")
end_date_str = end_date.strftime("%m/%d/%Y")
# # (Optional) Display the formatted date range to the user
# st.write(f"Filtering data from {start_date_str} to {end_date_str}")

# Define start and end dates from the selected date range
# start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    
# Filter data within the selected date range
filtered_data = filtered_data[(filtered_data['reportingDate'] >= start_date) & (filtered_data['reportingDate'] <= end_date)]

if filtered_data.empty:
    genai_trigger = 0
    st.error("There is no data in the selected date range.")
    filtered_data = data
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
        
else:
    genai_trigger = 1
    # If form is submitted, use filtered data; otherwise, default to  data.
    table1, table2, table3 = summarize_data(filtered_data)
    if submit_button:
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
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents= generate_prompt(table1, table2, table3))
        summary_placeholder.markdown(f"**Summary:**\n{response.text}")

    else:
        filtered_data = data
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



# Create a map using the filtered (or full) dataset

# # add llm module
# st.header("AI Summary")
# # Button to trigger the summary generation
# ai_submit_button = st.button("Generate Summary")

# # Placeholder to show the summary
# summary_placeholder = st.empty()

# # create prompt
# if ai_submit_button:
#     if genai_trigger == 0:
#         summary_placeholder.markdown("Selected data doesn't exist")
#     else:
#         client = genai.Client(api_key=api_key)
#         response = client.models.generate_content(
#         model="gemini-2.0-flash", contents= generate_prompt(table1, table2, table3))
#         summary_placeholder.markdown(f"**Summary:**\n{response.text}")



# Convert the filtered DataFrame to CSV format without the index
csv_data = filtered_data.to_csv(index=False)
 
# Create a download button for exporting the filtered data as a CSV file
st.download_button(
    label="Export Data",
    data=csv_data,
    file_name="filtered_data.csv",
    mime="text/csv"
)

#Total case count metric
total_observations = filtered_data['country'].count()
st.write("Total case observations:", total_observations)        

#Top country table
country_counts = data.groupby('country').size().reset_index(name='cases')
top_countries = country_counts.sort_values(by='cases', ascending=False).head(3)

#Top dates table - Yijun
date_counts = data.groupby('reportingDate').size().reset_index(name='observation_counts')
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
