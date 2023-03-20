import streamlit as st
import pandas as pd
import numpy as np

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
