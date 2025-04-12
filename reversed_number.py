def reverse(number):
    reversed_number = int(str(abs(number))[::-1])  # 轉成字串後反轉
    if number < 0:
        reversed_number = -reversed_number  # 若是負數，保持負號
    print(reversed_number)


# 測試程式
reverse(3456)