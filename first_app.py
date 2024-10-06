import streamlit as st
import streamlit.components.v1 as stc
import numpy as np
import pandas as pd
import random
import plotly.express as px
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

# dataframe
st.write('DataFrame')
df = pd.DataFrame({
    '一列目': [1,2,3,4],
    '二列目': [10,20,30,40]
})
st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=400, height=200)

# chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), 
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# map
map_data=pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [35.68, 138.59],
    columns=['lat', 'lon']
)
st.map(map_data)

def radar_chart():  
    df = pd.DataFrame(dict(
    r=[random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22)],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    placeholder.write(fig)

radar_chart()

button = st.button('run')
if button:
    audio_path1='keep_it_up.wav'
    audio_placeholder=st.empty()
    file_=open(audio_path1, "rb")
    contents=file_.read()
    file_.close()

    audio_str="data:audio/ogg;base64, %s"%(base64.b64encode(contents).decode())
    audio_html= '''
                    <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not support the audio element.
                    </audio>
                ''' %audio_str

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
