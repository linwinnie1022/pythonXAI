import streamlit as st

# ========= 初始化 session_state =========
if "cart" not in st.session_state:
    st.session_state.cart = []

# ========= 重新整理按鈕（最上面） =========
if st.button("重新整理"):
    st.rerun()

# ========= 標題 =========
st.title("點餐機")
st.write("請輸入餐點")

# ========= 輸入餐點 + 加入按鈕 =========
col1, col2 = st.columns([3, 1])

with col1:
    food = st.text_input("", key="food_input")  # ← 不顯示「餐點名稱」

with col2:
    if st.button("加入"):
        if food != "":
            st.session_state.cart.append(food)
            st.rerun()

st.write("---")

# ========= 購物籃 =========
st.subheader("購物籃")

# 只有購物籃有東西才顯示
if len(st.session_state.cart) > 0:
    for i, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(item)

        with col2:
            if st.button("刪除", key=f"del_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()

                # 算數指定運算子
a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0
a //= 2  # a = a // 2
print(a)  # 0
a %= 2  # a = a % 2
print(a)  # 0.0
a **= 2  # a = a ** 2
print(a)  # 0.0
