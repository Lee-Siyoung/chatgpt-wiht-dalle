import streamlit as st
import openai
from PIL import Image


st.set_page_config(
    page_title = "ChatGPT with DALL-E",
    page_icon="👋"
)
img = Image.open('img/style.png')
img2 = Image.open('img/style_niji.png')
img3 = Image.open('img/quality.png')
img4 = Image.open('img/stylize.png')
st.write("# Welcome to image create Web! 👋")


st.write(
    """
    ### This web is an image generation web using streamlit.
    
    
    ## Introduction to Parameters
    
    1. size : It's the image size
    2. count : Number of images
    3. Aspect Ratio : An aspect ratio is the width-to-height ratio of an image
    4. style : 
        - Midjourney : null, Raw
        - Niji : null, Cute, Expressive, Scenic
    """
)

st.image(img)
st.image(img2)
st.write(
    """
    5. Quality : The Quality parameter changes how much time is spent generating an image
    """
)

st.image(img3)
st.write(
    """
    6. Stylize : Low stylization values produce images that closely match the prompt but are less artistic. High stylization values create images that are very artistic but less connected to the prompt.
    """
)
st.image(img4)

