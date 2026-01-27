import streamlit as st

st.title("數字金字塔")
number = st.number_input("請輸入一個整數(1到9):", min_value=1, max_value=9, step=1)
st.write("數字金字塔:")

for i in range(1, int(number) + 1):
    st.write(str(i) * i)
