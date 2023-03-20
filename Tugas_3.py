import streamlit as st
import pandas as pd
import numpy as np
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
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
 
st.subheader("Container :")
