from streamlit_extras.colored_header import colored_header
import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("modified_laptops.csv")

colored_header(
    label="_SELECT THE LAPTOP FEATURES :_",
    description="",
    color_name="green-70",)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

# Selectbox inputs for laptop features :

Brand = st.selectbox("Select the Brand:: ", df["Brand"].unique())
Processor = st.selectbox("Select the Processor:: ", df["Processor"].unique())
ram_type = st.selectbox("Select the RAM Type:: ", df["RAM Type"].unique())
ram_size = st.selectbox("Select the RAM Size (GB)::", df["RAM"].unique())
Operating_system = st.selectbox("Select the os:: ", df["Operating System"].unique())
Storage = st.selectbox("Select the Storage size:: ", df["Storage"].unique())
Storage_type = st.selectbox("Select the Storage type:: ", df["Storage Type"].unique())

# Filter the dataset based on user inputs :
filtered_df = df[(df["Brand"] == Brand) &
                 (df["Processor"] == Processor) &
                 (df["RAM"] == ram_size) & 
                 (df["RAM Type"] == ram_type) & 
                 (df["Storage"] == Storage) & 
                 (df["Operating System"] == Operating_system) &
                 (df["Storage Type"] == Storage_type)]


st.text("")
st.text("")
st.text("")
st.text("")


colored_header(
    label="**FINALLY THE PREDICTED PRICE IS::**",
    description="",
    color_name="blue-70",)


# Calculate the average price for the filtered dataset :
avg_price = filtered_df["MRP"].mean()

# Display the predicted price :
st.subheader(f":blue[_Estimated Price:_]  {round(avg_price, 2)} INR")
