import streamlit as st

st.title("數字金字塔")
number = st.number_input("請輸入一個整數(1到9):", min_value=1, max_value=9, step=1)
st.write("數字金字塔:")

for i in range(1, int(number) + 1):
    st.write(str(i) * i)

n = st.number_input("請輸入箭頭的層數", min_value=1, step=1)

a = ""
for i in range(1, n + 1):
    a = a + (" " * (n - i) + "*" * (i * 2 - 1) + "\n")

for i in range(1, n + 1):
    a = a + (" " * (n - 1) + "*" + "\n")

st.write(f"```\n箭頭金字塔:\n{a}```")
