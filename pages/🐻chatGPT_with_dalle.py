import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT - DALL-E")
st.write(
    """
    ### ChatGPT automatically describes the features.
    """
)
with st.form("form"):
    user_input = st.text_input("Prompt")
    st.subheader("Parameter")
    size=st.radio("size", ["1024x1024", "512x512", "256x256"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    num = st.radio("count", ["1", "2", "3", "4"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Aspect = st.radio("Aspect Ratio", ["1:1", "3:4", "4:5", "9:16", "5:4", "4:3"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Quality = st.radio("Quality", ["1", ".25", ".5"])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Stylize = st.slider("select Stylize", 0, 1000, [100])
    
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [{
        "role" : "system",
        "content" : "Imagine the detail appeareance of the input. Response it shortly around 20 words."
    }]
    gpt_prompt.append({
        "role" : "user",
        "content" : user_input
    })
    
    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = gpt_prompt
        )
    
    prompt=gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)
    prompt = f"{prompt} and Parameter : [Aspect:{Aspect}, Quality:{Quality}, Stylize:{Stylize}]"
    
    with st.spinner("Waiting for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size,
            n=int(num)
        )
        
    for i in range(int(num)):
        st.image(dalle_response['data'][i]['url'])