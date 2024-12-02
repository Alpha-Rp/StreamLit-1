import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Simple data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    # reading it like a pandas dataframe
    df=pd.read_csv(uploaded_file)
    
    
    # displaying a subtitle
    st.subheader("Data Preview")
    
    # writing the dataframe
    st.write(df.head()) #the .head() will give you the first 5 rows frm the df
    
    # for summary 
    st.subheader("Data Summary")
    st.write(df.describe())
    
    # filtereing the data
    st.subheader("Filter Data")
    # passing sm widgits so the user can interact 
    columns = df.columns.tolist() #gives all columns in a python list
    selected_column = st.selectbox("Select column to filter by",columns)
    
    # grabbing all the unique values from this column
    unique_value=df[selected_column].unique()
    # slecting a column within a column
    selected_value = st.selectbox("Select value",unique_value)
    
    # its grabbing all the rows , where the dataframe at the selected column  = selected value
    filtered_df = df[df[selected_column]==selected_value]
    st.write(filtered_df)
    
    # plotting the graph
    st.subheader("plot data")
    
    # selecting x and y axis
    x_column = st.selectbox("select x-axis columns",columns)
    y_column = st.selectbox("select y-axis columns",columns)
    
    # generating a line chart
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else :
    st.write("waiting on file upload...")
    
    
     
    
    
    
    