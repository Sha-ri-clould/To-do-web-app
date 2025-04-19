import streamlit as st
from PIL import Image as Image,ImageOps
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
        if cam_image :
            camera_image=Image.open(cam_image)
            return camera_image
def upload():
    with st.expander('Tap to Upload Image'):
        uploaded_file = st.file_uploader("Upload Image",type=["png","jpg","jpeg"])
        if uploaded_file:
            uploaded_image=Image.open(uploaded_file)
            return uploaded_image
def download(d1_img):
    # Convert image to bytes for download
    buffer = BytesIO()
    d1_img.save(buffer, format="PNG")
    byte_img = buffer.getvalue()

    # Display download button
    st.download_button(
        label="Download Image",
        data=byte_img,
        file_name="converted_image.png",
        mime="image/png"
    )
   # Save image to internal storage
    save_path = os.path.join(os.getcwd(), "converted_image.png")
    d1_img.save(save_path)
    st.success(f"Image saved to {save_path}")

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
                download(d_img)

        if options=="Posterize Image":
            if img:
                img = img.convert("RGB")
                bits=st.slider("Select Posterize Image level",2,8,4,help="Higher bits more colors! Lower bits more abstract!")
                result=ImageOps.posterize(img,bits)
                st.text('Posterize Image')
                st.image(result,use_container_width=True)
                d_img=result
                download(d_img)


        if options=="Negative image":
            if img:
                img=np.array(img.convert("RGB"))
                invert=255-img
                pic=Image.fromarray(invert)
                st.text('Negative Image')
                st.image(pic,use_container_width=True)
                d_img=pic
                download(d_img)


