import streamlit as st

st.title("簡易購物平台")

products = ["apple", "banana", "bg", "orange"]
price = 10
image_folder = "image"

# 初始化庫存
if "stock" not in st.session_state:
    st.session_state.stock = {}
    for p in products:
        st.session_state.stock[p] = 10

cols_num = st.number_input(
    "一排顯示幾個商品", min_value=1, max_value=5, value=4, step=1
)

cols = st.columns(cols_num)

# ===== 商品區 =====
for i, product in enumerate(products):
    col = cols[i % cols_num]

    with col:
        st.image(f"image/{product}.png", width=150)
        st.write(f"商品名稱：{product}")
        st.write(f"價格：{price}")
        st.write(f"庫存：{st.session_state.stock[product]}")

        if st.button(f"購買 {product}", key=f"buy_{product}"):
            if st.session_state.stock[product] > 0:
                st.session_state.stock[product] -= 1
                st.rerun()  # ⭐ 關鍵
            else:
                st.error("庫存不足")

# ===== 新增庫存區 =====
st.subheader("新增商品庫存")

col1, col2 = st.columns(2)

with col1:
    select_product = st.selectbox("選擇商品", products)

with col2:
    add_num = st.number_input("新增庫存數量", min_value=1, step=1)

if st.button("新增庫存"):
    st.session_state.stock[select_product] += add_num
    st.rerun()  # ⭐ 關鍵

# ===== 目前庫存 =====
st.write("目前商品庫存:")

for p in products:
    st.write(f"{p}：{st.session_state.stock[p]}")
