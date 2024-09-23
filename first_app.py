import streamlit as st
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
#

st.subheader('subheader')
st.text('text text text')

code = '''
import streamlit as st

st.title('sample application')
'''

st.code(code, language='python')
