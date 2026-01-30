import streamlit as st
import openai  # pip install openai

# from utils import load_openai_api

openai.api_key = st.secrets["OPENAI_API_KEY"]  # 設定OpenAI的API金鑰

if "history" not in st.session_state:  # 初始化對話紀錄
    st.session_state.history = []  # 如果對架路不存在，創建一個空列表

if "system_message" not in st.session_state:  # 初始化系統訊息
    st.session_state.system_message = (
        "請用繁體中文進行後續對話"  # 如果系統訊息不存在，設置預設系統訊系
    )

if "model" not in st.session_state:  # 初始AI模型
    st.session_state.model = "gpt-4o-mini"  # 如果AI模型不存在，設置預設模型


# 設置三個列布局
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    # 在第一列縣市並更新系統訊息
    st.session_state.system_message = st.text_input(
        "系統訊息", st.session_state.system_message
    )

with col2:
    # 在第二列顯示並選擇AI模型
    st.session_state.model = st.selectbox(
        "AI模型",
        [
            "gpt-4o-mini",
            "gpt-4o",
            "gpt-4o-search-preview",
        ],
    )


with col3:
    if st.button("🗑️"):  # 在第三列顯示清空按鈕
        st.session_state.history = []  # 按下按鈕後清空對話紀錄
        st.rerun()  # 重新整理頁面已反映更改

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的回應")

for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪄").write(message["content"])
    else:
        st.chat_message("assistant", avatar="✨").write(message["content"])

prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model=st.session_state.model,
        messages=[{"role": "system", "content": "請用繁體中文進行後續對話"}]
        + st.session_state.history,
    )
    assistant_message = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()  # 重新整頁面顯示新訊息
