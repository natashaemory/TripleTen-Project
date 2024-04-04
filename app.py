import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header('Scatterplot of price vs. days listed with car type as color')

scatter2 = px.scatter(data, x='days_listed', y='price', color='type', title='Price by Days Listed with Car Type as Color',
                 labels={'days_listed': 'Days Listed', 'price': 'Price ($)', 'type': 'Type'})

st.plotly_chart(scatter2, use_container_width=True)





st.header('Compare odometer (miles) distributions between car conditions')

condition_types = data['condition'].unique().tolist()

condition_checkboxes = {condition: st.checkbox(f"Show {condition} Condition") for condition in condition_types}

filtered_data = data[data['condition'].isin([condition for condition, checked in condition_checkboxes.items() if checked])]

histogram = px.histogram(filtered_data, x='odometer', color='condition', title='Histogram of Odometer Miles with Condition as Color',
                         labels={'odometer': 'Odometer (miles)', 'condition': 'Condition'})

# Display the plot
st.plotly_chart(histogram, use_container_width=True)





