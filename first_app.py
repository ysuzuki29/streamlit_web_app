import streamlit as st
import streamlit.components.v1 as stc
import base64
import time
from PIL import Image


st.title('Lifestyle-related Disease Improvement Support App')
st.caption('Diabetic Support')

image = Image.open('oishii3_ojisan.png')
st.image(image, width=200)

name = st.text_input('name')
print(name)

submit_btn = st.button('submit')
cancel_btn = st.button('cancel')
print(f'submit_btn: {submit_btn}')
print(f'cancel_btn: {cancel_btn}')


button = st.button('run')
if button:
    audio_path1='keep_it_up.wav'
    audio_placeholder=st.empty()
    file_=open(audio_path1, "rb")
    contents=file_.read()
    file_.close()

    audio_str="data:audio/ogg;base64, %s"%(base64.b64encode(contents).decode())
    audio_html=%audio_str

audio_placeholder.empty()
time.sleep(0.5)
audio_placeholder.markdown(audio_html, unsafe_allow_html=True)

#

st.subheader('subheader')
st.text('text text text')

code = '''
import streamlit as st

st.title('sample application')
'''

st.code(code, language='python')
