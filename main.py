import streamlit as st
import pandas as pd


data=pd.read_csv("F:/2_Coding/Python/Steamlit/GUI_streamlit_using_csv/2021_Cars_Aggregated.csv")



lowest=min(data['OBFCM Fuel consumption (l/100 km)'])
highest=max(data['OBFCM Fuel consumption (l/100 km)'])
values = st.slider('Select a range of values',lowest, highest, (lowest, highest))
lval=values[0]
hval=values[1]

filtered_df = data.loc[(data['OBFCM Fuel consumption (l/100 km)'] <= hval) & (data['OBFCM Fuel consumption (l/100 km)'] >= lval) ]
st.scatter_chart(data=filtered_df, x='OBFCM Fuel consumption (l/100 km)', y='Manufacturer',color='Fuel Type')