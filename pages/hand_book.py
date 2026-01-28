import streamlit as st
import os

folderPath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderPath)  # 取得資料夾內所有檔案
# 這時候資料夾可能包含其他檔案，我們只需要 .md 檔案
files_name = []  # 新增清單用來存放 .md 的檔案
for f in files:  # 逐一檢查所有檔案，看看是否以 .md 結尾
    if f.endswith(".md"):  # 如果檔案名稱以 .md 結尾
        # if ".md" in f:  # 如果檔案名稱中包含 .md
        files_name.append(f)  # 將檔案名稱加入清單

files_name.sort()  # 將清單排序，預設是由小到大

for f in files_name:  # ['class1.md', 'class2.md']逐一讀取所有 .md 檔案
    # 用with open()讀取檔案內容並存到file變數裡面，模式為r，檔案編碼為utf-8
    # 這樣可以不用擔心檔案讀取後忘記關閉的問題
    # open參數格式為(檔案路徑, 檔案模式, 檔案編碼)
    # markdown\class2.md
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        # 開啟檔案後可以做很多事情，這裡我們只讀取檔案內容
        content = file.read()

    with st.expander(f[:-3]):  # 使用expander，標題為檔案名稱去掉.md
        st.markdown(content)  # 將檔案內容顯示在網頁上
    # file = open(f"{folderPath}/{f}", "r", encoding="utf-8")
    # content = file.read()
    # file.close()
    # f = 'class1.md' 可以用list的方式取得檔案名稱的每個字元
    # f[0]  c
    # f[1]  l
    # f[2]  a
    # f[3]  s
    # f[4]  s
    # f[5]  1
    # f[6]  .  f[-3]
    # f[7]  m  f[-2]
    # f[8]  d  f[-1]
