def my_find(sub, full):
    sub_len = len(sub)
    full_len = len(full)

    for i in range(full_len - sub_len + 1):
        if full[i:i + sub_len] == sub:
            return i 
    return -1 

s1 = input("請輸入第一個字串：")
s2 = input("請輸入第二個字串：")

# 執行程式
pos = my_find(s1, s2)

if pos != -1:
    print(f"'{s1}' 是 '{s2}' 的子字串")
else:
    print(f"'{s1}' 不是 '{s2}' 的子字串")
