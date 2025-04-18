import streamlit as st
from PIL import Image as image,ImageOps
import os
import numpy as np

os.makedirs(".streamlit",exist_ok=True)
custom_theme="""[theme]
primaryColor="#4d78da"
backgroundColor="#000000"
secondaryBackgroundColor="#8e8ecb"
textColor="#bee867"
"""
with open(".streamlit/config.toml","w") as f:
    f.write(custom_theme)

st.title('Play with Pictures!')
st.markdown("<i>Converts Image into Grey-Scale image , Posterize image and Negative image.</i>",unsafe_allow_html=True)

options=st.radio("Choose filter",["Grey scale image","Negative image","Posterize Image"])

if options=="Grey scale image":
    with st.expander('Tap to Open Camera'):
        camera_image=st.camera_input("Take a Picture")

    if camera_image:
        img=image.open(camera_image)
        grey_img=img.convert('L')
        st.text('Grey Scale Image')
        st.image(grey_img,use_container_width=True)

if options=="Posterize Image":
    with st.expander('Tap to Open Camera'):
        camera_image = st.camera_input("Take a Picture")

    if camera_image:
        img=image.open(camera_image)
        bits=st.slider("Select Posterize Image",2,8,4,help="Higher bits more colors! Lower bits more abstract!")
        result=ImageOps.posterize(img,bits)
        st.text('Posterize Image')
        st.image(result,use_container_width=True)

if options=="Negative image":
    with st.expander('Tap to Open Camera'):
        camera_image=st.camera_input("Take a picture")

    if camera_image:
        img=image.open(camera_image)
        img=np.array(img.convert("RGB"))
        invert=255-img
        pic=image.fromarray(invert)
        st.text('Negative Image')
        st.image(pic,use_container_width=True)
