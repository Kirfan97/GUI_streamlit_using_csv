import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("Upload a CSV File", type="csv")
if uploaded_file is not None:
    # Reading the uploaded CSV file
    data = pd.read_csv(uploaded_file)
    st.write("Here's your uploaded data:")
    st.dataframe(data)
    missing_val=data.isnull().sum()
    st.header('Missing Analysis')
    st.write(missing_val)

    with st.sidebar:
        #Scatter plot option
        st.header("Scatter Plot")
        x_option = st.selectbox(
        'What column would be the x input?',
        (data.columns),key=1)
        y_option = st.selectbox(
        'What column would be the y input?',
        (data.columns),key=2)
        c_option = st.selectbox(
        'What column would be the color input?',
        (data.columns),index=None,placeholder="Select the legend for the graph",key=3)

    st.header("Scatter Plot")
    st.scatter_chart(data=data, x=x_option, y=y_option,color=c_option)

    


