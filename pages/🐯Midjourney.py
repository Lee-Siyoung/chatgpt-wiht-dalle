import streamlit as st
import openai 

openai.api_key = st.secrets["api_key"]

st.title("Midjourney")

with st.form("form"):
    Prompt = st.text_input("Prompt")
    st.subheader("Parameter")
    size=st.radio("size", ["1024x1024", "512x512", "256x256"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    num = st.radio("count", ["1", "2", "3", "4"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Aspect = st.radio("Aspect Ratio", ["1:1", "3:4", "4:5", "9:16", "5:4", "4:3"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    style = st.radio("style", ["null", "Raw"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Quality = st.radio("Quality", ["1", ".25", ".5"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Stylize = st.slider("select Stylize", 0, 1000, [100])
    
    Prompt = f"an image of Midjourney: {Prompt}, Parameter : [Aspect:{Aspect}, style:{style}, Quality:{Quality}, Stylize:{Stylize}]"
    submit = st.form_submit_button("Submit")
    
    
if submit and Prompt:
    with st.spinner("Waiting for Midjourney..."):
        Midjourney_response = openai.Image.create(
            prompt=Prompt,
            size=size,
            n=int(num)
        )
            
    for i in range(int(num)):
        st.image(Midjourney_response['data'][i]['url'])