import streamlit as st

st.header("Phinyo Sabai")

st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('นายภิญโญ สบาย')
st.subheader('สาขาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./Pic/yo.jpg')
with col2:
    st.image('./Pic/flower.jpg')

html_1 = """
<div style="background-color:#FFFAFA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:#FFFFFF">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

dt=pd.read_csv('./Data/iris.csv')
st.write(dt.head(10))
