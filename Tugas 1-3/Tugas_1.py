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