import streamlit as st
import pandas as pd
import numpy as np

"""
# Tugas 1 : Dataframe dan AreaChart

"""
import streamlit as st
import pandas as pd
st.subheader("Nilai UAS dan UTS Matematika")

df_data = pd.DataFrame({
'Name' : ["Susan", "Budi", "Yanto", "Chika"],
  'UTS': [85, 75, 95, 40],
  'UAS': [70, 80, 80, 65]
})
st.table(df_data)

st.subheader("Area chart:")

st.write("Nilai UAS dan UTS Matematika")
area_data = pd.DataFrame({
'Name' : ["Susan", "Budi", "Yanto", "Chika"],
  'UTS': [85, 75, 95, 40],
  'UAS': [70, 80, 80, 65],
})

area_data = area_data.set_index('Name')
st.area_chart(area_data)
"""
# Tugas 2 

"""
st.subheader("Database Nilai UTS dan UAS Data Science :")
import streamlit as st
import pandas as pd
df = pd.DataFrame({
'Name' : ["Susan", "Budi", "Yanto", "Chika"],
  'UTS': [85, 75, 95, 40],
  'UAS': [70, 80, 80, 65]
})
df

st.subheader("Grafik Nilai UAS dan UTS  Data Science :")
WR = pd.DataFrame({
    'UAS': [70, 80, 80, 65],
    'UTS': [85, 75, 95, 40]
})
st.line_chart(WR)

agree = st.checkbox('I agree')

if agree:
    st.write('Thanks You')

col1, col2 = st.columns([3, 1])
col1.subheader("A wide column with a chart")
col1.line_chart(WR)

col2.subheader("A narrow column with the data")
col2.write(df)
