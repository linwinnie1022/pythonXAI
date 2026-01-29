import random  # 匯入random模組

x = random.randrange(1, 100 + 1)
min = 1
max = 100
while True:
    a = int(input(f"請輸入{min}到{max}的整數"))
    if a < x:
        print("太小了！")
        min = a
    elif a > x:
        print("太大了！")
        max = a
    else:
        print("答對了！")
        break
