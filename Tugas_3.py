import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

'''
# Tugas 3
'''

st.subheader("1. Write and Magic :")

st.subheader("Write : ")
st.write('Hello William')

st.subheader("Magic : ")
'''
# *_Hello William_*
'''

st.subheader("2. Text Element :")
st.markdown('This Game is **_really_ cool**.')

st.subheader("3. Data Dispaly Element :")
df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)

st.subheader("4. Chart Element :")
df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))
st.area_chart(df)

st.subheader("5. Input Widget Element :")
age = st.slider('How old are you?', 0, 100, 50)
st.write("I'm ", age, 'years old')

st.subheader("6. Media Element :")
image = Image.open('./magic circle1.png')

st.image(image, caption='# Magic Circle')

st.subheader("7. Layout & Container :")
st.subheader("Layout :")
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A Magic Circle")
   st.image("./magic circle1.png")

with col2:
   st.header("A Barrier_Circle")
   st.image("./magic_circle.png")

with col3:
   st.header("A Aura Circle")
   st.image("./shield_Edit.png")
 
st.subheader("Container :")
container = st.container()
container.write("This is inside the container")
st.write("This is outside the container")

container.write("This is inside too")


st.subheader("8. Status Element :")

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
   
progres = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(75):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progres)
