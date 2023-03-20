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
# Tugas 2 :  
Latihan 1 : Chart , Widget , Layout

"""
st.subheader("Nilai UAS dan UTS Matematika:")
import streamlit as st
import pandas as pd
df = pd.DataFrame({
'Name' : ["Susan", "Budi", "Yanto", "Chika"],
  'UTS': [85, 75, 95, 40],
  'UAS': [70, 80, 80, 65]
})
df

st.subheader("Line Chart : ")
st.subheader("Grafik Nilai UAS dan UTS  Matematika :")
WR = pd.DataFrame({
    'UAS': [70, 80, 80, 65],
    'UTS': [85, 75, 95, 40]
})
st.line_chart(WR)

st.subheader("Widget : ")
nilai = st.slider('Berapa Nilai UAS Matematika :', 0, 100, 50)
st.write('Nilai UAS saya adalah : ', nilai)
nilai1 = st.slider('Berapa Nilai UTS Matematika :', 0, 100, 50)
st.write('Nilai UAS saya adalah : ', nilai1)

agree = st.checkbox('I agree')

if agree:
    st.write('Thanks You')

st.subheader("Layout : ")
col1, col2 = st.columns([3, 1])
col1.subheader("A wide column with a chart")
col1.line_chart(WR)

col2.subheader("A narrow column with the data")
col2.write(df)


"""

# Tugas 2 :  
Latihan 2 : Chart , Widget , Layout

"""

@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} mendapat nilai uas :{row.UAS}: dan nilai uts :{row.UTS}:")
