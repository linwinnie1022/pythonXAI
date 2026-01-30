# for 迴圈
# for 會搭配 in 來使用， in 後面接一個有範圍的東西
# range(5) 會產生 0, 1, 2, 3, 4 不包含5
# i 是迴圈的變數可以自己取名
# 迴圈變數每回合會從範圍裏面取一個資料出來
for i in range(5):
    print(i)

# range 可以設定起始值與結束值， 但不會包含結束直
# range(1, 5) 會產生 1, 2, 3, 4
for j in range(1, 5):
    print(j)

# range 可以設定起始值、結束值與間隔值, 但不會包含結束值
# range(1, 10, 2) 會產生 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)

for i in range(5):
    print(i)

for i in range(5):
    a = i * 2  # 將i程已2並存入a
print(a)  # 在終端機顯示a所存的值


x = int(input())
y = int(input())
for z in range(x, y + 1):
    print(f"{z}號在教室")
