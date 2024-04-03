import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('/Users/natashagandhi/Desktop/TripleTen-Project/vehicles_us.csv')

st.header('Scatterplot of price vs. days listed with car type as color', divider='black')

scatter2 = px.scatter(data, x='days_listed', y='price', color='type', title='Price by Days Listed with Car Type as Color',
                 labels={'days_listed': 'Days Listed', 'price': 'Price ($)', 'type': 'Type'})

st.plotly_chart(scatter2, use_container_width=True)





st.header('Compare odometer (miles) distributions between car conditions', divider='black')

histogram1 = px.histogram(data, x='odometer', color='condition', title='Histogram of Odometer Miles with Condition as Color',
                   labels={'odometer': 'Odometer (miles)', 'condition': 'Condition'})

show_condition = st.checkbox("Show Car Condition Type")

#Only display the plot if the checkbox is checked
if show_condition:
    st.plotly_chart(histogram1, use_container_width=True)






