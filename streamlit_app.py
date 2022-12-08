import streamlit as st
import pandas as pd
import base64
from PIL import Image

st.title("HELLO SEXY")
st.header("media files")


st.markdown('''
This the video source of porn collection :[meganz](https://mega.nz/fm/7lFmQRha)''')

image= Image.open('h.jpg')
st.image(image,caption='hot lana')

def add_bg_from_url():
    st.markdown(



         f"""
         <style>
         .stApp {{
             background-image: url("https://ftopx.com/images/202103/ftopx.com_605472607f088.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
