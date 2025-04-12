def most_frequent_numbers():
    nums = input("請輸入一連串正整數（以空格分隔）：").split()
    count_dict = {}

    # 統計每個數字的出現次數
    for num in nums:
        if num.isdigit():
            num = int(num)
            count_dict[num] = count_dict.get(num, 0) + 1
        else:
            print(f"忽略無效輸入：{num}")

    # 找出最大出現次數
    if count_dict:
        max_count = max(count_dict.values())
        most_frequent = [num for num, count in count_dict.items() if count == max_count]

        print(f"\n出現最多次的數字：{', '.join(map(str, most_frequent))}")
        print(f"出現次數：{max_count} 次")
    else:
        print("沒有有效的正整數輸入")

# 執行程式
most_frequent_numbers()
