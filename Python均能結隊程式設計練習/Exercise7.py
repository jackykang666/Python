def sumDigits(n):
    if n < 10:
        return n
    else:
        return sumDigits(n // 10) + (n % 10)

# 執行程式
num = int(input("請輸入一個正整數："))
if num >= 0:
    print(f"{num} 的數字總和為：{sumDigits(num)}")
else:
    print("請輸入正整數！")
