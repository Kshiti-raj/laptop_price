import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page

#TITLE AND IMAGE
col1, col2, col3 = st.columns([2,6,1])
with col1:
    st.write("")
with col2:
    st.header(":desktop_computer: **:green[TESLA]**  _:blue[laptops]_ :desktop_computer: ")
with col3:
    st.write("")

# centering the image:
left_co, cent_co,last_co = st.columns(3)
with left_co:
    st.image("laptop6.jpg",width=700)
    

st.text("")
st.text("")
# customizing the buttons used:
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(150,100,100);
}
</style>""", unsafe_allow_html=True)


# BUTTON
if st.button("!! Tap here !! "):
    st.header(" :orange[ WELCOMEE TO Tesla laptops interface!!!] :raised_hand_with_fingers_splayed: ")
    st.balloons()
st.text("")
st.text("")
st.text("")
st.text("")

#coloring the header:
colored_header(
    label="_The New Icon:_",
    description="",
    color_name="violet-70",)


st.text("")
st.text("")
st.text("")

col1, col2 ,col3= st.columns(3)
with col1:
    st.image("laptop7.jpg")
with col2:
    st.image("tesla log.jpg")
with col3:
    st.image("laptop4.jpg")


st.text("")
st.text("")
st.text("")


colored_header(
    label="",
    description="",
    color_name="green-90",)

st.text(" ")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")


# RADIO
reply = st.radio(
    "WOULD YOU LIKE TO MOVE ON TO THE NEXT PAGE ?",
    ("\"yes\"","\"no\""))

st.text("")
st.text("")

if reply == "\"yes\"":
    move_page = st.button("I want to move pages!")
    if move_page:
        switch_page("Data Proof")
if reply == "\"no\"":
    st.text("I think you should!!")

    st.text("")
    st.text("")
    st.text(" ")


st.text(" ")
st.text(" ")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text(" ")
st.text("")
st.text("")
st.text(" ")
st.text(" ")
st.text("")
st.text("")

# DOWNLOAD IMAGES
              
col1,col2,col3, col4= st.columns(4)
with col1:
    with open("laptop6.jpg","rb") as file :
        btn = st.download_button(
                label="**Download image 1**",
                data=file,
                file_name="laptop6.jpg",
                mime="image/jpg")

with col2:
    with open("laptop7.jpg", "rb") as file:
        btn = st.download_button(
                label="**Download image 2**",
                data=file,
                file_name="laptop6.jpg",
                mime="image/jpg")
    


with col3:
    with open("tesla log.jpg", "rb") as file:
        btn = st.download_button(
                label="**Download image 3**",
                data=file,
                file_name="tesla log.jpg",
                mime="image/jpg")
    

with col4:
    with open("laptop4.jpg", "rb") as file:
        btn = st.download_button(
                label="**Download image 4**",
                data=file,
                file_name="laptop4.jpg",
                mime="image/jpg")
        

st.text(" ")
st.text(" ")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text(" ")
st.text("")
st.text("")
st.text(" ")
st.text(" ")
st.text("")
st.text("")

col1, col2 ,col3= st.columns([2,2,1])
with col1:
    st.text("")
with col2:
    st.text("")
with col3:
    st.text("MADE BY- KSHITI RAJ")


