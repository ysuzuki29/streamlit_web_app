import streamlit as st
import streamlit.components.v1 as stc
import numpy as np
import pandas as pd
import random
#import plotly
#import plotly.express as px
import base64
import time
from PIL import Image
import json
import wave
import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect('example.db')
c = conn.cursor()

# テーブルの作成
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, mealname TEXT, calorie INTEGER)''')
 
# データの挿入
if st.button("データを挿入"):
    c.execute("INSERT INTO users (mealname, calorie) VALUES (?, ?)", ("hamburger", 100))
    c.execute("INSERT INTO users (mealname, calorie) VALUES (?, ?)", ("curry", 200))
    c.execute("INSERT INTO users (mealname, calorie) VALUES (?, ?)", ("gyudon", 300))
    c.execute("INSERT INTO users (mealname, calorie) VALUES (?, ?)", ("oatmeal", 400))
    c.execute("INSERT INTO users (mealname, calorie) VALUES (?, ?)", ("gohan", 500))
    c.execute("INSERT INTO users (mealname, calorie) VALUES (?, ?)", ("pizza", 600))
    c.execute("INSERT INTO users (mealname, calorie) VALUES (?, ?)", ("udon", 700))
    c.execute("INSERT INTO users (mealname, calorie) VALUES (?, ?)", ("sushi", 800))
    conn.commit()
    st.write("データが挿入されました")
 
# データの取得
c.execute("SELECT * FROM users")
rows = c.fetchall()
 
# データの表示
st.write("ユーザー情報:")
for row in rows:
    st.write(row)
 
# 接続を閉じる
conn.close()


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

name = st.text_input('name', placeholder="your name")
st.write("Hi! ",name)

age = st.text_input('age', placeholder="your age")
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

height=1
weight=1
height = st.text_input('height', placeholder="your height (m)")
st.write(height)

weight = st.text_input('weight', placeholder="your weight (kg)")
st.write(weight)

bmi=float(weight)/(float(height)*float(height))

st.write("your BMI is ", bmi)

bmi_class=['x<=18.5', '18.5<x<25', '25<x<30', '30<x<35', '35<x<40', '40<x']
who_ref=['Underweight', 'Normal range', 'Pre-obese', 'Obese class 1', 'Obese class 2', 'Obese class 3']

# dataframe
st.write('DataFrame')
df = pd.DataFrame({
    'BMI (kg/m^2)': bmi_class,
    'WHO reference': who_ref
})
st.write(df)

st.write("You are in ")
if bmi <= 18.5:
    st.write(who_ref[0])
elif bmi <=25:
    st.write(who_ref[1])
elif bmi <=30:
    st.write(df[1,2])
elif bmi <=35:
    st.write(df[1,3])
elif bmi <=40:
    st.write(df[1,4])
else: st.write(df[1,5])


#st.dataframe(df.style.highlight_max(axis=0), width=400, height=200)

st.write("What meals did you eat today?")

st.write('examples: hamburger, curry, oatmeal, gyudon, pizza, udon, sushi, gohan')

def showMealPicture(mealname):
    if mealname=='hamburger':
        st.image(image_hamburger, width=200)
    elif mealname=='curry':
        st.image(image_curry, width=200)
    elif mealname=='oatmeal':
        st.image(image_oatmeal, width=200)
    elif mealname=='gyudon':
        st.image(image_gyudon, width=200)
    elif mealname=='pizza':
        st.image(image_pizza, width=200)
    elif mealname=='udon':
        st.image(image_udon, width=200)
    elif mealname=='sushi':
        st.image(image_sushi, width=200)
    else:
        st.image(image_gohan, width=200)
  

breakfast = st.text_input('breakfast')
st.write(breakfast)
showMealPicture(breakfast)

lunch = st.text_input('lunch')
st.write(lunch)
showMealPicture(lunch)

supper = st.text_input('supper')
st.write(supper)
showMealPicture(supper)

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
    #fig = px.line_polar(df, r='r', theta='theta', line_close=True)
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
