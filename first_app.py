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
import math
import datetime
#from openai import OpenAI

#for i in range(1,10,1):
#    st.write(math.factorial(i))

# SQLiteデータベースに接続
conn = sqlite3.connect('meal_data.db')
c = conn.cursor()
conn_p = sqlite3.connect('personal_data.db')
c_p = conn_p.cursor()

# テーブルの作成
c.execute('''CREATE TABLE IF NOT EXISTS meal_data
             (id INTEGER PRIMARY KEY, name TEXT, calorie INTEGER, GI REAL)''')

c_p.execute('''CREATE TABLE IF NOT EXISTS personal_data
             (id INTEGER PRIMARY KEY, name TEXT, gender TEXT, age INTEGER, height REAL, weight REAL)''')
 
# データの挿入
if st.button("データを挿入"):
    c.execute("INSERT INTO meal_data (name, calorie, GI) VALUES (?, ?, ?)", ("hamburger", 294.9, 80))
    c.execute("INSERT INTO meal_data (name, calorie, GI) VALUES (?, ?, ?)", ("curry", 650, 90))
    c.execute("INSERT INTO meal_data (name, calorie, GI) VALUES (?, ?, ?)", ("gyudon", 716, 75))
    c.execute("INSERT INTO meal_data (name, calorie, GI) VALUES (?, ?, ?)", ("oatmeal", 350, 60))
    c.execute("INSERT INTO meal_data (name, calorie, GI) VALUES (?, ?, ?)", ("gohan", 168, 85))
    c.execute("INSERT INTO meal_data (name, calorie, GI) VALUES (?, ?, ?)", ("pizza", 872, 83))
    c.execute("INSERT INTO meal_data (name, calorie, GI) VALUES (?, ?, ?)", ("udon", 727, 93))
    c.execute("INSERT INTO meal_data (name, calorie, GI) VALUES (?, ?, ?)", ("sushi", 640, 91))
    conn.commit()
    st.write("データが挿入されました")

if st.button("データを挿入 personal data"):
    c_p.execute("INSERT INTO personal_data (name, gender, age, height, weight) VALUES (?, ?, ?, ?, ?)", ("Yoshimi Suzuki", "male", 61, 1.75, 64)) 
    c_p.execute("INSERT INTO personal_data (name, gender, age, height, weight) VALUES (?, ?, ?, ?, ?)", ("Hanako", "female", 48, 1.60, 55)) 
    c_p.execute("INSERT INTO personal_data (name, gender, age, height, weight) VALUES (?, ?, ?, ?, ?)", ("Taro", "male", 55, 1.70, 80)) 
    conn_p.commit()

# データの取得
c.execute("SELECT * FROM meal_data")
rows = c.fetchall()

c_p.execute("SELECT * FROM personal_data")
rows_p = c_p.fetchall()


# データの表示
st.write("料理とカロリー:")
for row in rows:
    st.write(row)

name_dict={}
persons=[]
st.write("個人データ:")
for row_p in rows_p:
    st.write(row_p) # personal_data 
    st.write(row_p[1]) # personoal_data name
    name_dict[row_p[1]]=row_p[0]
    persons.append(pd.Series(row_p))
    #st.write(row_p)
st.write(name_dict)
st.write(persons)

#c.execute("SELECT * FROM meal_data WHERE name='curry'")
#d=c.fetchone()
#st.write("calorie of ", d[1], " is", d[2], "kcal")

#c_p.execute("SELECT * FROM personal_data WHERE name='Yoshimi Suzuki'")
#d_p=c_p.fetchone()
#st.write("You are ", d_p[1], "years old")

# 接続を閉じる
#conn.close()


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
if name in name_dict:
    st.write("You are already registered!!")
    for person in persons:
        if person[1]==name:
            gender=person[2]
            age=person[3]
            height=person[4]
            weight=person[5]
            st.write("age=", age, "gender=", gender, "height=", height, "weight=", weight)
else:
    st.write("Please register now.")
    age = st.text_input('age', placeholder="your age")
    st.write("You are ", age)

    gender = st.radio(
        "gender: (male|female)",
        ["male", "female"],
    )

    st.write(gender)
    if gender=='male':
        st.image(image_oji, width=200)
    else:
        st.image(image_oba, width=200)

    height = st.text_input('height', placeholder="your height (m)")
    st.write(height)

    weight = st.text_input('weight', placeholder="your weight (kg)")
    st.write(weight)
    submit_btn = st.button('submit')
    cancel_btn = st.button('cancel')
    print(f'submit_btn: {submit_btn}')
    print(f'cancel_btn: {cancel_btn}')

    new_person=[name, gender, age, height, weight]
    c_p.execute("INSERT INTO personal_data (name, gender, age, height, weight) VALUES (?, ?, ?, ?, ?)", (name, gender, int(age), float(height), float(weight))) 
    st.write("age=", age, "gender=", gender, "height=", height, "weight=", weight)
    conn_p.commit()

def float2string(float_num):
    return "{:.2f}".format(float_num)

bmi=float(weight)/(float(height)*float(height))
st.write("your BMI is ", float2string(bmi))

bmi_class=['x<=18.5', '18.5<x<25', '25<x<30', '30<x<35', '35<x<40', '40<x']
who_ref=['Underweight', 'Normal', 'Pre-obese', 'Obese class 1', 'Obese class 2', 'Obese class 3']

# dataframe
st.write('DataFrame')
df = pd.DataFrame({
    'BMI (kg/m^2)': bmi_class,
    'WHO reference': who_ref
})
st.write(df)

if bmi <= 18.5:
    st.write("You are in", who_ref[0], "level")
elif bmi <=25:
    st.write("**You are in", who_ref[1], "level**")
elif bmi <=30:
    st.write("You are in", who_ref[2], "level")
elif bmi <=35:
    st.write("You are in", who_ref[3], "level")
elif bmi <=40:
    st.write("You are in", who_ref[4], "level")
else: st.write("You are in", who_ref[5], "level")
st.write("***") # horizontal line

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

def ideal_calorie(gender, age, height, weight, activitiy_level):
    if(gender=="male"):
        param=0.4235
    else:
        param=0.9708
    ideal_cal=(0.0481*weight+0.0234*height*100-0.0138*age-param)*1000/4.186*(1.25+activitiy_level*0.25)
    return ideal_cal

st.write("ideal calorie=", float2string(ideal_calorie(gender, age, height, weight, 3)))

st.write("***") # horizontal line

total_calorie=0
cals=[]
meals=[]

# breakfast
breakfast = st.radio(
    "breakfast: ",
    ["hamburger", "curry", "oatmeal", "gyudon", "pizza", "udon", "sushi", "other"], horizontal=True,
)
if breakfast == "other":
    breakfast = st.text_input('breakfast')

st.write(breakfast)
showMealPicture(breakfast)
c.execute("SELECT * FROM meal_data WHERE name=?", (breakfast, ))
d=c.fetchone()
st.write("calorie of ", d[1], " is", d[2], "kcal")
total_calorie+=d[2]
cals.append(d[2])
meals.append('breakfast')

# lunch
lunch = st.radio(
    "lunch: ",
    ["hamburger", "curry", "oatmeal", "gyudon", "pizza", "udon", "sushi", "other"], horizontal=True,
)
if lunch == "other":
    lunch = st.text_input('lunch')

st.write(lunch)
showMealPicture(lunch)
c.execute("SELECT * FROM meal_data WHERE name=?", (lunch, ))
d=c.fetchone()
st.write("calorie of ", d[1], " is", d[2], "kcal")
total_calorie+=d[2]
cals.append(d[2])
meals.append('lunch')

# supper
supper = st.radio(
    "supper: ",
    ["hamburger", "curry", "oatmeal", "gyudon", "pizza", "udon", "sushi", "other"], horizontal=True,
)
if supper == "other":
    supper = st.text_input('supper')

st.write(supper)
showMealPicture(supper)
c.execute("SELECT * FROM meal_data WHERE name=?", (supper, ))
d=c.fetchone()
st.write("calorie of ", d[1], " is", d[2], "kcal")
total_calorie+=d[2]
cals.append(d[2])
meals.append('supper')

# snack
snack = st.radio(
    "snack: ",
    ["hamburger", "curry", "oatmeal", "gyudon", "pizza", "udon", "sushi", "other"], horizontal=True,
)
if snack == "other":
    supper = st.text_input('snack')

st.write(snack)
showMealPicture(snack)
c.execute("SELECT * FROM meal_data WHERE name=?", (snack, ))
d=c.fetchone()
st.write("calorie of ", d[1], " is", d[2], "kcal")
total_calorie+=d[2]
cals.append(d[2])
meals.append('snack')

st.write("today's total calorie is ", total_calorie, "kcal")

######
submit_btn = st.button('submit')
cancel_btn = st.button('cancel')
print(f'submit_btn: {submit_btn}')
print(f'cancel_btn: {cancel_btn}')

# dataframe
st.write('DataFrame')
df = pd.DataFrame({
    'meal': ['breakfast','lunch','supper','snack', 'total', 'ideal'],
    'calorie(kcal)': [cals[0],cals[1],cals[2],cals[3],total_calorie,ideal_calorie(gender,age,height,weight,3)]
})
#st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=400, height=300)

meal_calorie=pd.DataFrame(cals, meals)
st.bar_chart(meal_calorie)


#
def chat():
    with st.chat_message("User"):
        st.write("Hello, Assistant")

    with st.chat_message("Assistant"):
        st.write("Hello User")
        st.bar_chart(np.random.randn(30,3))


    prompt=st.chat_input("Hello. Say somethong")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")


    st.title("Hello Bot")
    if "Messages" not in st.session_state:
        st.session_state.messages=[]

    for message in st.session_state.messages:
        with st.chat_message(message("role")):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

    response=f"Echo: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)
#

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})


#-------------------

# chart
def chart():
    chart_data = pd.DataFrame(
        np.random.randn(20,3), 
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

# map
def map():
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

def audio():
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

# 接続を閉じる
conn.close()
conn_p.close()

