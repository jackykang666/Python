def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

# 執行程式
m = int(input("請輸入第一個整數 m："))
n = int(input("請輸入第二個整數 n："))

result = gcd(m, n)
print(f"{m} 和 {n} 的最大公因數是：{result}")
