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