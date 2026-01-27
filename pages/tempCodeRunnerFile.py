x = float(input("請輸入身高(m)"))
y = int(input("請輸入體重(kg)"))
bmi = y / x**2
if bmi < 18.5:
    print("過輕")
elif 18.5 <= bmi < 24:
    print("正常")
else:
    print("過重")
