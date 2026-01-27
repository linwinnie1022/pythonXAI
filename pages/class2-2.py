import streamlit as st  # 匯入streamlit模組並重新命名為st

# st.number_input()可以讓使用者輸入數字，設定step=1可以讓使用者只能輸入整數
# min_value=0可以設定最小值為0，max_value=100可以設定最大值為100
number = st.number_input("請輸入一個數字:", step=1, min_value=0, max_value=100)
# st.markdown()可以在網頁使用markdown語法顯示文字
if number >= 90:
    st.write("你的等級為A")
elif 80 <= number < 90:
    st.write("你的等級為B")
elif 70 <= number < 80:
    st.write("你的等級為C")
elif 60 <= number < 70:
    st.write("你的等級為D")
else:
    st.write("你的等級為F")

st.markdown("---")
st.markdown("### 按鈕練習")
# st.button()可以在網頁上顯示一個按鈕，使用者可以點及按鈕
# key式按鈕的識別名稱，可以用來區分不同的按鈕
# 如果使用者點及按鈕，st.button()會回傳True，否則回傳False
st.button("按我一下", key="button1")
if st.button("按我一下", key="button2"):
    st.balloons()
if st.button("按我一下", key="snow"):
    st.snow()
st.markdown("---")

st.title("奇偶數判斷器")
number = st.number_input("請輸入一個整數:", step=1)
if number % 2 == 0:
    st.write("你輸入的是**偶數**")
else:
    st.write("你輸入的是**奇數**")
