import streamlit as st
import time

with st.spinner("正在努力處理中，請稍後..."):
    time.sleep(3)

st.success("完成啦！")
