from streamlit_extras.colored_header import colored_header
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

#display the dataframe:
st.header(f":blue['THE DATAFRAME:']")
data = pd.read_csv("modified_laptops.csv")
df = pd.DataFrame(data)
st.dataframe(df)

chart_data = pd.DataFrame(df)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

colored_header(
    label="_VISUAL PRESENTATION:_",
    description="",
    color_name="violet-70",)

st.text("")
st.text("")


# OPTIONS FOR VIEWING PLOTS :
option = st.radio(
    "**Which plot would you like to view ?. Select one from below!!**",
    ('MRP/RAM',"MRP/OS","MRP/STORAGE","MRP/PROCESSOR","MRP/STORAGE TYPE"))

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

if option == 'MRP/RAM':
    st.header(f':green[Here\'s the plot between MRP/RAM :]')
    st.bar_chart(chart_data,x="RAM",y ="MRP")
if option == 'MRP/OS':
    st.header(f':green[Here\'s the plot between MRP/OS :]')
    st.bar_chart(chart_data,x="Operating System",y ="MRP")
if option == 'MRP/STORAGE':
    st.header(f':green[Here\'s the plot between MRP/STORAGE :]')
    st.bar_chart(chart_data,x="Storage",y ="MRP")
if option == 'MRP/PROCESSOR':
    st.header(f':green[Here\'s the plot between MRP/PROCESSOR :]')
    st.bar_chart(chart_data,x="Processor",y ="MRP")
if option == 'MRP/STORAGE TYPE':
    st.header(f':green[Here\'s the plot between MRP/STORAGE TYPE :]')
    st.bar_chart(chart_data,x="Storage Type",y ="MRP")


m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(150,100,100);
}
</style>""", unsafe_allow_html=True)


# RADIO
reply = st.radio(
    "WOULD YOU LIKE TO MOVE ON TO THE LAST PAGE ?",
    ("\"yes\"","\"no\""))
st.text("")
st.text("")
st.text("")

if reply == "\"yes\"":
    move_page = st.button("I want to move pages!")
    if move_page:
        switch_page("Price prediction")
if reply == "\"no\"":
    st.text("I think you should!!")