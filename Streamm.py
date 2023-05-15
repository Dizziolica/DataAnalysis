
import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit for financial Programing')
st.header('Streamlit header')
st.subheader('Streamlit sub header')
st.write("My content be written here!")
st.caption('Caption are here!')

df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})
st.write(df)
x = st.sidebar.slider('x', 0, 10)
st.write(x*x)
if st.sidebar.checkbox('Checkbox'):
    st.balloons()

y = st.sidebar.text_input('Name')
st.write(y)
st.number_input('Number', 50,  100)
st.date_input('Date Input')
option = st.selectbox('Wich number do you list best?', [1, 2, 3, 4])
st.write('You selected', option)

char_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(char_data)
left, right = st.columns(2)
left.write('I am the left Side!')
with right:
    st.write('I am the Right Side!')

tab1, tab2, tab3 = st.tabs(['Streamlit1','Streamlit2', 'Streamlit3'])

with tab1:
    st.header('First tab')

with tab2:
    st.header('Second Tab')

with tab3:
    st.header('Third Tab')

import time
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
