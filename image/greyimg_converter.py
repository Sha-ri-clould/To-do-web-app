import streamlit as st
from PIL import Image as image
import os

os.makedirs(".streamlit",exist_ok=True)
custom_theme="""[theme]
primaryColor="#4d78da"
backgroundColor="#000000"
secondaryBackgroundColor="#8e8ecb"
textColor="#bee867"
"""
with open(".streamlit/config.toml","w") as f:
    f.write(custom_theme)

st.title('Greyscale Image Converter')
st.markdown("<i>Converts Image into Grey-Scale image</i>",unsafe_allow_html=True)

with st.expander('Tap to Open Camera'):
    camera_image=st.camera_input("Take a Picture")

if camera_image:
    img=image.open(camera_image)
    grey_img=img.convert('L')
    st.text('Grey Scale Image')
    st.image(grey_img)