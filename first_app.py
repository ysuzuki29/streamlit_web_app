import streamlit as st
import streamlit.components.v1 as stc
import numpy as np
import pandas as pd
import random
import plotly
import plotly.express as px
import base64
import time
from PIL import Image
import json
import wave


st.title('Lifestyle-related Disease Improvement Support App')
st.caption('Diabetic Support')

image = Image.open('seikatsusyukan_lowcalorie.png')
image_oji = Image.open('oishii3_ojisan.png')
image_oba = Image.open('bentou_obasan.png')

image_hamburger = Image.open('food_hamburger_cheese.png')
image_curry = Image.open('curry_indian_man.png')
image_gyudon = Image.open('food_gyudon.png')
image_oatmeal = Image.open('food_oatmeal.png')
image_gohan = Image.open('food_gohan.png')
image_pizza = Image.open('pizza_margherita.png')
image_udon = Image.open('food_udon.png')
image_sushi = Image.open('nigirizushi_moriawase.png')

st.image(image, width=200)

name = st.text_input('name')
st.write("Hi! ",name)

age = st.text_input('age')
st.write(age)

gender = st.radio(
    "gender: (male|female)",
    [":rainbow[male]", "***female***"],
)

st.write(gender)
if gender==':rainbow[male]':
    st.image(image_oji, width=200)
else:
    st.image(image_oba, width=200)

st.write('examples: hamburger, curry, oatmeal, gyudon, pizza, udon, sushi, gohan')

breakfast = st.text_input('breakfast')
st.write(breakfast)
if breakfast=='hamburger':
    st.image(image_hamburger, width=200)
elif breakfast=='curry':
    st.image(image_curry, width=200)
elif breakfast=='oatmeal':
    st.image(image_oatmeal, width=200)
elif breakfast=='gyudon':
    st.image(image_gyudon, width=200)
elif breakfast=='pizza':
    st.image(image_pizza, width=200)
elif breakfast=='udon':
    st.image(image_udon, width=200)
elif breakfast=='sushi':
    st.image(image_sushi, width=200)
else:
    st.image(image_gohan, width=200)

lunch = st.text_input('lunch')
st.write(lunch)
if lunch=='hamburger':
    st.image(image_hamburger, width=200)
elif lunch=='curry':
    st.image(image_curry, width=200)
elif lunch=='oatmeal':
    st.image(image_oatmeal, width=200)
elif lunch=='gyudon':
    st.image(image_gyudon, width=200)
elif lunch=='pizza':
    st.image(image_pizza, width=200)
elif lunch=='udon':
    st.image(image_udon, width=200)
elif lunch=='sushi':
    st.image(image_sushi, width=200)
else:
    st.image(image_gohan, width=200)

supper = st.text_input('supper')
st.write(supper)
if supper=='hamburger':
    st.image(image_hamburger, width=200)
elif supper=='curry':
    st.image(image_curry, width=200)
elif supper=='oatmeal':
    st.image(image_oatmeal, width=200)
elif supper=='gyudon':
    st.image(image_gyudon, width=200)
elif supper=='pizza':
    st.image(image_pizza, width=200)
elif supper=='udon':
    st.image(image_udon, width=200)
elif supper=='sushi':
    st.image(image_sushi, width=200)
else:
    st.image(image_gohan, width=200)

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
    #audio_placeholder.write(fig)

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

audio_placeholder = st.empty()
time.sleep(0.5)
#
#

st.subheader('subheader')
st.text('text text text')

code = '''
import streamlit as st

st.title('sample application')
'''

st.code(code, language='python')
