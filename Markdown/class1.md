太好了，今天學的內容其實很多 👍
我幫你**整理成一份「國小四年級也看得懂」的 Python 筆記**，用簡單的說法＋小例子，像上課重點整理一樣。

---

## 🐍 Python 上課重點筆記（四年級版）

---

## 一、註解（給人看的說明文字）

👉 **註解不會被電腦執行，只是給人看**

### 1️⃣ 單行註解

```python
# 這是單行註解
```

### 2️⃣ 多行註解

```python
"""
這是多行註解
可以寫很多行
"""
```

💡 小技巧：
`Ctrl + /` 可以快速註解或取消註解

---

## 二、print（顯示文字或數字）

👉 `print()` 可以把東西顯示在畫面上

```python
print("Hello World!")
print(123)
```

---

## 三、資料的種類（基本型態）

| 種類  | 名稱   | 例子         | 說明       |
| ----- | ------ | ------------ | ---------- |
| int   | 整數   | 1、0、-5     | 沒有小數點 |
| float | 小數   | 1.5、3.14    | 有小數點   |
| str   | 文字   | "apple"      | 要加引號   |
| bool  | 布林值 | True / False | 只有對或錯 |

```python
print(1)
print(1.23)
print("apple")
print(True)
```

---

## 四、變數（像盒子一樣存東西）

👉 變數就是**幫資料取名字**

```python
a = 10
print(a)

a = "apple"
print(a)
```

📦 `=` 的意思是「把右邊的東西放進左邊的盒子」

---

## 五、數學運算（跟算數一樣）

| 符號 | 意思   |
| ---- | ------ |
| +    | 加     |
| -    | 減     |
| \*   | 乘     |
| /    | 除     |
| //   | 取商   |
| %    | 取餘數 |
| \*\* | 次方   |

```python
print(2 + 3)
print(2 ** 3)  # 2的3次方
```

### 🧠 運算順序（很重要）

1. () 括號
2. \*\* 次方
3. - / // %
4. - -

---

## 六、字串（文字）的小技巧

### 1️⃣ 字串相加

```python
print("apple" + " pen")
```

### 2️⃣ 字串乘法

```python
print("ha" * 3)
```

---

## 七、f-string（把變數放進文字）

👉 可以讓文字更聰明

```python
name = "apple"
age = 10
print(f"我叫{name}，我今年{age}歲")
```

---

## 八、len() 和 type()

### 1️⃣ len()：算字有幾個

```python
print(len("apple"))  # 5
```

### 2️⃣ type()：看資料是什麼種類

```python
print(type(1))
print(type("apple"))
```

---

## 九、型態轉換（資料變身）

👉 有時要把資料換成別的種類

```python
int(1.5)      # 變成整數
float(1)      # 變成小數
str(100)      # 變成文字
bool(1)       # 變成 True
```

⚠️ 文字如果不是數字，不能變成數字

```python
# int("hello")  # 會出錯
```

---

## 十、input()（讓使用者輸入）

👉 **使用者輸入的東西一定是「文字」**

```python
a = input("請輸入一些文字:")
print(a)
```

如果要算數學，要先轉成整數：

```python
print(int(a) + 10)
```

---

## 十一、實用小練習

### 📐 算圓的面積

```python
r = int(input("請輸入半徑:"))
pi = 3.14
area = pi * r**2
print(area)
```

### 📚 算平均成績

```python
x = int(input("期中成績:"))
y = int(input("期末成績:"))
print((x + y) / 2)
```

### 💪 BMI 計算

```python
h = int(input("身高(cm):")) / 100
w = int(input("體重(kg):"))
bmi = w / (h**2)
print(bmi)
```

---

## 十二、Streamlit（做簡單網頁）

👉 Streamlit 可以把 Python 變成網頁

```python
import streamlit as st
```

### 常用指令

```python
st.title("標題")
st.write("可以顯示很多東西")
st.text("只能顯示純文字")
st.markdown("可以用Markdown")
```

---

## 🌟 小總結

✔ 今天你學會了

- 顯示文字
- 存資料
- 算數學
- 讓使用者輸入
- 做小工具
- 還能做網頁！
