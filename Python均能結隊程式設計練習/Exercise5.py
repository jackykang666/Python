def assign_grade(score, best):
    if score >= best - 10:
        return 'A'
    elif score >= best - 20:
        return 'B'
    elif score >= best - 30:
        return 'C'
    elif score >= best - 40:
        return 'D'
    else:
        return 'F'

# 讀取使用者輸入
scores_input = input("Enter scores separated by spaces from one line: ")
scores = list(map(int, scores_input.split()))

# 找出最高分
best = max(scores)

# 顯示每位學生的成績與等級
for i, score in enumerate(scores):
    grade = assign_grade(score, best)
    print(f"Student {i} score is {score} and grade is {grade}")
