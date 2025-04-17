students = {}

def add_student():
    name = input("請輸入學生姓名：")
    scores = {}
    for subject in ["數學", "英文", "科學"]:
        score = float(input(f"請輸入 {name} 的 {subject} 成績："))
        scores[subject] = score
    students[name] = scores
    print(f"已新增學生 {name} 的成績。\n")

def calculate_total_and_average(scores):
    total = sum(scores.values())
    average = total / len(scores)
    return total, average

def query_student():
    name = input("請輸入要查詢的學生姓名：")
    if name in students:
        scores = students[name]
        total, average = calculate_total_and_average(scores)
        print(f"\n{name} 的成績如下：")
        for subject, score in scores.items():
            print(f"{subject}:{score}")
        print(f"總分：{total}, 平均：{average:.2f}\n")
    else:
        print("找不到此學生！\n")

def list_all_students():
    if not students:
        print("⚠ 尚無任何學生資料。\n")
        return

    student_list = []
    for name, scores in students.items():
        total, average = calculate_total_and_average(scores)
        student_list.append((name, total, average))

    # 依照總分由高到低排序
    student_list.sort(key=lambda x: x[1], reverse=True)

    print("\n📋 所有學生成績概覽（依總分排序）：")
    for name, total, average in student_list:
        print(f"{name}：總分 = {total}, 平均 = {average:.2f}")
    print()

def class_average():
    if not students:
        print("⚠ 尚無任何學生資料。\n")
        return

    subject_totals = {"數學": 0, "英文": 0, "科學": 0}
    student_count = len(students)

    for scores in students.values():
        for subject in subject_totals:
            subject_totals[subject] += scores[subject]

    print("\n📊 各科全班平均分數：")
    for subject, total in subject_totals.items():
        print(f"{subject} 平均：{total / student_count:.2f}")
    print()

def main_menu():
    while True:
        print("===== 學生成績管理系統 =====")
        print("1. 新增學生與成績")
        print("2. 查詢特定學生成績")
        print("3. 顯示所有學生成績（排序）")
        print("4. 顯示全班平均分數")
        print("5. 離開系統")
        choice = input("請選擇功能 (1-5)：")

        if choice == "1":
            add_student()
        elif choice == "2":
            query_student()
        elif choice == "3":
            list_all_students()
        elif choice == "4":
            class_average()
        elif choice == "5":
            print("系統結束，謝謝使用！")
            break
        else:
            print("請輸入有效選項！\n")

# 執行主選單
main_menu()
