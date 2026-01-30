好，這裡我幫你整理成**「國小四年級也看得懂」的超簡單筆記版** ✨
我會用👉重點＋例子＋一句話記憶法 的方式來寫，你可以直接拿去背、抄、教同學都 OK。

---

# 🧠 Python 超簡單筆記（四年級版）

---

## 一、什麼是「變數」？

👉 **變數就是用來裝資料的盒子**

```python
length = 5
```

📦 盒子名字：`length`
📦 裡面的東西：`5`

---

## 二、全域變數 vs 區域變數

### ✅ 全域變數（大家都看得到）

- 寫在**函數外面**
- 整個程式都可以用

```python
length = 5  # 全域變數
```

---

### ✅ 區域變數（只有函數裡看得到）

- 寫在**函數裡面**
- 出了函數就不見了

```python
def calculate():
    area = length * length  # area 是區域變數
```

❌ 這樣會錯：

```python
print(area)  # 看不到！
```

🧠 **記憶法**
👉「區域變數＝教室裡的秘密，出教室就不知道了」

---

## 三、為什麼在函數裡不能直接改全域變數？

❌ 這樣會出錯：

```python
def calculate():
    length = length + 1
```

📌 因為 Python 會以為你在用「新的盒子」

---

## 四、正確拿到函數算出來的結果（用 return）

### ✅ 最推薦、最安全的方法 ⭐⭐⭐

```python
def calculate_square_area():
    area = length * length
    return area

length = 5
area = calculate_square_area()
print(area)  # 25
```

🧠 **記憶法**
👉「要東西就用 return 拿出來」

---

## 五、global（⚠️ 不太推薦，新手看看就好）

```python
def calculate():
    global area
    area = length * length
```

📌 可以改全域變數
⚠️ 但容易搞亂，不建議常用

---

## 六、函數是什麼？

👉 **函數＝會幫你做事情的小機器**

```python
def hello(name):
    print("Hello", name)
```

使用：

```python
hello("Alice")
```

💬 印出：

```
Hello Alice
```

---

## 七、參數是什麼？

```python
def hello(name):
```

👉 `name` 是**參數**
👉 參數也是「區域變數」

---

## 八、AI 對話（超簡單概念）

### 📌 AI 聊天需要三樣東西

1️⃣ API 金鑰（像鑰匙）
2️⃣ messages（聊天紀錄）
3️⃣ model（AI 的大腦）

```python
messages = [
    {"role": "user", "content": "你好"}
]
```

---

## 九、Streamlit 是什麼？

👉 **把 Python 變成網頁畫面**

### 顯示聊天泡泡

```python
st.chat_message("user").write("你好")
st.chat_message("assistant").write("哈囉")
```

---

### 記住聊天內容（很重要！）

```python
st.session_state.history = []
```

👉 不然一重新整理就會忘記

---

## 十、常見小工具

### ⏳ 等待動畫

```python
with st.spinner("處理中..."):
    time.sleep(3)
```

### ✅ 成功提示

```python
st.success("完成啦！")
```

---

## 十一、AI 產生圖片（知道就好）

👉 輸入一句話
👉 AI 幫你畫圖

```python
prompt = "A cute baby sea otter"
```

---

## 🌟 超重要總整理（一定要背）

🟡 **全域變數**：寫在外面，大家都能用
🟡 **區域變數**：寫在函數裡，只有裡面能用
🟡 **return**：把結果帶出來
🟡 **函數**：幫你做事的小機器
🟡 **Streamlit**：把程式變成網頁

---
