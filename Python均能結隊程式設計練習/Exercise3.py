def series_sum():
    numerator = 1
    denominator = 3
    total = 0.0

    while numerator <= 97 and denominator <= 99:
        total += numerator / denominator
        numerator += 2
        denominator += 2

    return total

# 執行程式
result = series_sum()
print(f"數列總和為：{result:}")