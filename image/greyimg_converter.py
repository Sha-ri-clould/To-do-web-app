from tkinter import Image

import streamlit as st
from PIL import Image as image,ImageOps
import os
from io import BytesIO
import numpy as np

os.makedirs(".streamlit",exist_ok=True)
custom_theme="""[theme]
base="dark"
primaryColor="#d9fd00"
secondaryBackgroundColor="#292926"
textColor="#d7ff0c"
"""
with open(".streamlit/config.toml","w") as f:
    f.write(custom_theme)
def camera():
    with st.expander('Tap to Open Camera'):
        cam_image=st.camera_input("Take a picture")
        if(cam_image):
            camera_image=image.open(cam_image)
            return camera_image
def upload():
    with st.expander('Tap to Upload Image'):
        uploaded_file = st.file_uploader("Upload Image",type=["png","jpg","jpeg"])
        if uploaded_file:
            uploaded_image=image.open(uploaded_file)
            return uploaded_image
def download(dwn_image,name,type):
    enter=st.button("Download Image")
    if enter:
        save_path = rf"C:\Users\SHARIGA P\Pictures\image converter\{name}.{type.lower()}"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        dwn_image.save(save_path, type.lower())

        buf = BytesIO()
        dwn_image.save(save_path, type.lower())
        buf.seek(0)
        st.download_button(
            label="Download Image",
            data=buf,
            file_name=f"{name}.{type.lower()}",
            mime="image/jpeg",
        )
        st.success(f"Image saved to: {save_path}")
d_img=None
st.title('Play with Pictures!')
st.markdown("<i>Converts Image into Grey-Scale image , Posterize image and Negative image.</i>",unsafe_allow_html=True)
upload_option=st.selectbox("Select image input method",["Upload image","Use camera"])
if upload_option=="Use camera":
    img=camera()
else:
    img=upload()
if img:
    options=st.radio("Choose filter",["Grey scale image","Negative image","Posterize Image"])
    button=st.button("Convert")
    if button:
        if options=="Grey scale image":
            if img:
                grey_img=img.convert('L')
                st.text('Grey Scale Image')
                st.image(grey_img,use_container_width=True)
                d_img=grey_img

        if options=="Posterize Image":
            if img:
                bits=st.slider("Select Posterize Image level",2,8,4,help="Higher bits more colors! Lower bits more abstract!")
                result=ImageOps.posterize(img,bits)
                st.text('Posterize Image')
                st.image(result,use_container_width=True)
                d_img=result

        if options=="Negative image":
            if img:
                img=np.array(img.convert("RGB"))
                invert=255-img
                pic=image.fromarray(invert)
                st.text('Negative Image')
                st.image(pic,use_container_width=True)
                d_img=pic

if d_img is not None:
    st.subheader("Download your image here")
    download_name = st.text_input("Enter file name",key='name')
    download_type = st.radio("select image type", ["PNG", "JPG", "JPEG"],key='type')
    if download_type=="JPEG":
        download(d_img,download_name,download_type)